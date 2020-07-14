package org.quantil.quantme.simon.tasks;

import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.quantil.quantme.simon.config.Configuration;
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

public class RequestErrorMitigationTask extends SendMessageTask {
	
	private final static Logger LOGGER = LoggerFactory.getLogger(RequestErrorMitigationTask.class);
	
	private static final String OPERATION_NAME = "requestErrorMitigationTask";

	@Override
	protected Object generateRequest(DelegateExecution execution, String correlationId) {
		RequestErrorMitigationTask errorMitigationTask = new RequestErrorMitigationTask();
		// TODO
		return errorMitigationTask;
	}

	@Override
	protected String getOperationName() {
		return OPERATION_NAME;
	}

	@Override
	protected String getRequestUrl() {
		return Configuration.getInstance().properties.getProperty("provenance-service-rest-api-url");
	}
}
