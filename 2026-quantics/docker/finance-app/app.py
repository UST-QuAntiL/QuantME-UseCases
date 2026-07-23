# This code is a part of a Qiskit project
# Copyright IBM 2017, 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

from flask import Flask, jsonify, request
import datetime
import numpy as np

from qiskit.circuit.library import TwoLocal
from qiskit_aer.primitives import Sampler
from qiskit_algorithms import QAOA, SamplingVQE
from qiskit_algorithms.optimizers import COBYLA
from qiskit_algorithms.utils import algorithm_globals
from qiskit_finance.applications.optimization import PortfolioOptimization
from qiskit_finance.data_providers import RandomDataProvider, YahooDataProvider
from qiskit_optimization.algorithms import MinimumEigenOptimizer

app = Flask(__name__)


def build_portfolio_problem(num_assets, stocks, token, q, budget):
    seed = 123

    # If no stocks provided, auto-generate
    if not stocks:
        stocks = [f"TICKER{i}" for i in range(num_assets)]

    data = RandomDataProvider(
            tickers=stocks,
            start=datetime.datetime(2016, 1, 1),
            end=datetime.datetime(2016, 1, 30),
            seed=seed,
    )

    data.run()

    mu = data.get_period_return_mean_vector()
    sigma = data.get_period_return_covariance_matrix()

    portfolio = PortfolioOptimization(
        expected_returns=mu,
        covariances=sigma,
        risk_factor=q,
        budget=budget,
    )

    return portfolio.to_quadratic_program()


@app.route("/vqe", methods=["POST"])
def solve_vqe():
    print("solve vqe")
    try:
        print("vqe")
        body = request.get_json()

        num_assets = body.get("num_assets")
        stocks = body.get("stocks", [])
        token = body.get("token", None)
        q = body.get("q")
        budget = body.get("budget")
        reps = body.get("reps", 3)

        if not num_assets or q is None or budget is None:
            return jsonify({"error": "num_assets, q and budget are required"}), 400

        algorithm_globals.random_seed = 1234

        qp = build_portfolio_problem(num_assets, stocks, token, q, budget)

        cobyla = COBYLA()
        cobyla.set_options(maxiter=500)

        ansatz = TwoLocal(num_assets, "ry", "cz", reps=reps, entanglement="full")

        svqe_mes = SamplingVQE(
            sampler=Sampler(),
            ansatz=ansatz,
            optimizer=cobyla
        )

        optimizer = MinimumEigenOptimizer(svqe_mes)
        result = optimizer.solve(qp)
        print("final vqe")

        return jsonify({
            "algorithm": "VQE",
            "selection": result.x.tolist(),
            "value": float(result.fval)
        })

    except Exception as e:
        print("failed")
        return jsonify({"error": str(e)}), 500


@app.route("/qaoa", methods=["POST"])
def solve_qaoa():
    print("solve qaoa")
    try:
        print("execute qaoa")
        body = request.get_json()
        print("body")

        num_assets = body.get("num_assets")
        stocks = body.get("stocks", [])
        token = body.get("token", None)
        q = body.get("q")
        budget = body.get("budget")
        reps = body.get("reps", 3)
        print("body extracted")

        if not num_assets or q is None or budget is None:
            return jsonify({"error": "num_assets, q and budget are required"}), 400

        algorithm_globals.random_seed = 1234

        qp = build_portfolio_problem(num_assets, stocks, token, q, budget)
        print("qubo buikd")

        cobyla = COBYLA()
        cobyla.set_options(maxiter=250)

        qaoa_mes = QAOA(
            sampler=Sampler(),
            optimizer=cobyla,
            reps=reps
        )

        optimizer = MinimumEigenOptimizer(qaoa_mes)
        result = optimizer.solve(qp)
        print("final")

        return jsonify({
            "algorithm": "QAOA",
            "selection": result.x.tolist(),
            "value": float(result.fval)
        })

    except Exception as e:
        print("failed qoaa")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=False)
