package org.quantil.quantme.simon.tasks;

import java.net.MalformedURLException;
import java.net.URL;

import org.camunda.bpm.engine.delegate.BpmnError;
import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.quantil.quantme.simon.config.Configuration;
import org.quantil.quantme.simon.requests.ExpandOracleRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

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

public class RequestOracleExpansionTask extends SendMessageTask {
	
	private final static Logger LOGGER = LoggerFactory.getLogger(RequestOracleExpansionTask.class);
	
	private static final String OPERATION_NAME = "requestOracleExpansionTask";

	@Override
	protected Object generateRequest(DelegateExecution execution, String correlationId) {
		final ExpandOracleRequest request = new ExpandOracleRequest();
		request.setProgrammingLanguage(execution.getVariable("ProgrammingLanguage").toString());
		request.setOracleId(Integer.parseInt(execution.getVariable("OracleId").toString()));
		request.setQuantumCircuit((byte[]) execution.getVariable("QuantumCircuit"));
		try {
			request.setOracleCircuitUrl(new URL(execution.getVariable("oracleURL").toString()));
		} catch (MalformedURLException e) {
			LOGGER.error("Error while parsing URL: {}", execution.getVariable("oracleURL").toString());
			throw new BpmnError("Given oracle URL is invalid: " + execution.getVariable("oracleURL").toString());
		}
		return request;
	}

	@Override
	protected String getOperationName() {
		return OPERATION_NAME;
	}

	@Override
	protected String getRequestUrl() {
		return Configuration.getInstance().properties.getProperty("oracle-service-rest-api-url");
	}
}
