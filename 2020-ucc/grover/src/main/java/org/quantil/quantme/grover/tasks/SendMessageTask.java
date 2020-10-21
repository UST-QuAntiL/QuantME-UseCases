package org.quantil.quantme.grover.tasks;

import org.camunda.bpm.engine.delegate.BpmnError;
import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.camunda.bpm.engine.delegate.JavaDelegate;
import org.quantil.quantme.grover.config.Configuration;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

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

public abstract class SendMessageTask implements JavaDelegate {
	
	private final static Logger LOGGER = LoggerFactory.getLogger(SendMessageTask.class);
	
	/**
	 * Correlation ID to identify the response message in the receive task
	 */
    private String generateCorrelationId(DelegateExecution execution){
        return getOperationName() + "_" + execution.getProcessInstanceId();
    }
    
    /**
     * Camunda endpoint to receive callbacks
     */
    protected String getMessageEndPointUrl(){
        return String.format("%s/%s", Configuration.getInstance().properties.getProperty("engine-rest-api-url"), "message");
    }

    /**
     * Generate request for the specific send task depending on the target service 
     */
    protected abstract Object generateRequest(DelegateExecution execution, String correlationId);
    
    /**
     * Get the operation name of the send task to use it as part of the correlation ID
     */
    protected abstract String getOperationName();
    
    /**
     * Get the request URL for the service that should be invoked
     */
    protected abstract String getRequestUrl();

    /**
     * Generic method to invoke different services
     */
    public void execute(DelegateExecution execution) throws Exception {
    	LOGGER.info("Executing send task with name: {}", execution.getCurrentActivityName());

        final Object requestMessage = generateRequest(execution, generateCorrelationId(execution));
        final String requestUrl = getRequestUrl();
        LOGGER.info("Sending request to URL: {}", requestUrl);

        final Client client = ClientBuilder.newClient();
        try {
            final Response response = client.target(requestUrl)
                    .request(MediaType.APPLICATION_JSON)
                    .post(Entity.entity(requestMessage, MediaType.APPLICATION_JSON));

            LOGGER.info("Server responded with status code: {}", response.getStatus());
        } catch(Exception e) {
        	LOGGER.error("Exception while sending post request to URL: {}", requestUrl);
        	throw new BpmnError("Exception while sending post request to URL: " + requestUrl);
        }
    }
}
