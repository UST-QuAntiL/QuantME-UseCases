package org.quantil.quantme.demonstrator.tasks.classification;

import java.net.URL;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.camunda.bpm.engine.delegate.BpmnError;
import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.camunda.bpm.engine.delegate.JavaDelegate;
import org.json.JSONObject;
import org.quantil.quantme.demonstrator.Constants;
import org.quantil.quantme.demonstrator.Utils;
import org.quantil.quantme.demonstrator.config.Configuration;
import org.quantil.quantme.demonstrator.requests.classification.OptimizeSupportVectorsRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/********************************************************************************
 * Copyright (c) 2021 Institute of Architecture of Application Systems -
 * University of Stuttgart, Author: Benjamin Weder
 *
 * This program and the accompanying materials are made available under the
 * terms the Apache Software License 2.0 which is available at
 * https://www.apache.org/licenses/LICENSE-2.0.
 *
 * SPDX-License-Identifier: Apache-2.0
 ********************************************************************************/

public class OptimizeSupportVectorsTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(OptimizeSupportVectorsTask.class);

    @Override
    public void execute(DelegateExecution execution) throws Exception {
        LOGGER.info("Optimizing support vecotrs for the SVM iteration...");

        // get job id related to this workflow instance
        final int jobId = Integer
                .valueOf(execution.getVariable(Constants.VARIABLE_NAME_CLASSIFICATION_JOB_ID).toString());

        // get current iteration
        final int iterations = Integer
                .valueOf(execution.getVariable(Constants.VARIABLE_NAME_CLASSIFICATION_ITERATIONS).toString());

        // create request
        final OptimizeSupportVectorsRequest request = new OptimizeSupportVectorsRequest();
        request.setClassificationConfigUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_CLASSIFICATION_CONFIG_FILE));
        request.setResultsUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_CLASSIFICATION_RESULTS_FILE));
        request.setDeltaUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_CLASSIFICATION_DELTA_FILE));
        request.setThetasUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_CLASSIFICATION_THETA_FILE));
        request.setLabelsUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_CLUSTER_MAPPINGS_FILE));
        request.setIteration(iterations);

        // send request and retrieve result
        final String requestUrl = getRequestUrl(jobId);
        LOGGER.info("Sending request to URL: {}", requestUrl);
        final Client client = ClientBuilder.newClient();
        try {
            final Response response = client.target(requestUrl).request(MediaType.APPLICATION_JSON)
                    .post(Entity.entity(request, MediaType.APPLICATION_JSON));

            LOGGER.info("Server responded with status code: {}", response.getStatus());
            if (response.getStatus() != 200) {
                LOGGER.error("Status code does not equal 200, aborting: {}", response.getStatus());
                throw new BpmnError("Status code does not equal 200, aborting: " + response.getStatus());
            }

            // get URL for result objects
            final JSONObject jo = new JSONObject(response.readEntity(String.class));
            final Double costs = Double.valueOf(jo.get(Constants.CLASSIFICATION_RESPONSE_COSTS).toString());
            LOGGER.info("Current costs: {}", costs);
            final URL thetasUrl = new URL(jo.get(Constants.CLASSIFICATION_RESPONSE_THETAS_OUT_URL).toString());
            final URL thetasPlusUrl = new URL(jo.get(Constants.CLASSIFICATION_RESPONSE_THETAS_PLUS_URL).toString());
            final URL thetasMinusUrl = new URL(jo.get(Constants.CLASSIFICATION_RESPONSE_THETAS_MINUS_URL).toString());
            final URL deltaUrl = new URL(jo.get(Constants.CLASSIFICATION_RESPONSE_DELTA_URL).toString());

            // download results and add to variables
            boolean success = Utils.addFileFromUrlAsVariable(thetasUrl, "thetas-",
                    Constants.VARIABLE_NAME_CLASSIFICATION_THETA_FILE, MediaType.TEXT_PLAIN, execution);
            success &= Utils.addFileFromUrlAsVariable(thetasPlusUrl, "thetas-plus-",
                    Constants.VARIABLE_NAME_CLASSIFICATION_THETA_PLUS_FILE, MediaType.TEXT_PLAIN, execution);
            success &= Utils.addFileFromUrlAsVariable(thetasMinusUrl, "thetas-minus-",
                    Constants.VARIABLE_NAME_CLASSIFICATION_THETA_MINUS_FILE, MediaType.TEXT_PLAIN, execution);
            success &= Utils.addFileFromUrlAsVariable(deltaUrl, "deltas-",
                    Constants.VARIABLE_NAME_CLASSIFICATION_DELTA_FILE, MediaType.TEXT_PLAIN, execution);
            LOGGER.info("Downloading and adding of file returned: {}", success);

            // evaluate costs and number of iterations
            final boolean converged = iterations >= Constants.CLASSIFICATION_MAX_ITERATIONS
                    || costs < Constants.CLASSIFICATION_TARGET_COSTS;

            LOGGER.info("Result of convergence check: {}", converged);
            execution.setVariable(Constants.VARIABLE_NAME_CLASSIFICATION_CURRENT_COSTS, costs);
            execution.setVariable(Constants.VARIABLE_NAME_CLASSIFICATION_CONVERGED, converged);
        } catch (final Exception e) {
            e.printStackTrace();
            LOGGER.error("Exception while sending post request to URL: {}", requestUrl);
            throw new BpmnError("Exception while sending post request to URL: " + requestUrl);
        }
    }

    private String getRequestUrl(int jobId) {
        return Configuration.getInstance().properties.getProperty("classification")
                + Constants.CLASSIFICATION_API_OPTIMIZATION + jobId;
    }
}
