package org.quantil.quantme.simon.tasks;

import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.quantil.quantme.simon.config.Configuration;
import org.quantil.quantme.simon.requests.ExecuteCircuitRequst;

/********************************************************************************
 * Copyright (c) 2020 Institute for the Architecture of Application System -
 * University of Stuttgart
 * Author: Benjamin Weder
 *
 * This program and the accompanying materials are made available under the
 * terms the Apache Software License 2.0
 * which is available at https://www.apache.org/licenses/LICENSE-2.0.
 *
 * SPDX-License-Identifier: Apache-2.0
 ********************************************************************************/

public class RequestQuantumCircuitExecutionTask extends SendMessageTask {
	
	private static final String OPERATION_NAME = "requestCircuitExecutionTask";

	@Override
	protected Object generateRequest(DelegateExecution execution, String correlationId) {
		final ExecuteCircuitRequst request = new ExecuteCircuitRequst();
		request.setCorrelationId(correlationId);
		request.setReturnAddress(getMessageEndPointUrl());
		request.setProgrammingLanguage(execution.getVariable("QuantumProgrammingLanguage").toString());
		request.setProvider(execution.getVariable("Provider").toString());
		request.setQPU(execution.getVariable("QPU").toString());
		request.setAccessToken(execution.getVariable("ibmAccessToken").toString());
		request.setQuantumCircuit(execution.getVariable("QuantumCircuit").toString());
		return request;
	}

	@Override
	protected String getOperationName() {
		return OPERATION_NAME;
	}

	@Override
	protected String getRequestUrl() {
		return Configuration.getInstance().properties.getProperty("execution-service-rest-api-url");
	}
}
