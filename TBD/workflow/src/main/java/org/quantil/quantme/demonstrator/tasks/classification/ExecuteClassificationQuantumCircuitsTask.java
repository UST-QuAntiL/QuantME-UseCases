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
import org.quantil.quantme.demonstrator.requests.classification.ExecuteCircuitsRequest;
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

public class ExecuteClassificationQuantumCircuitsTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(ExecuteClassificationQuantumCircuitsTask.class);

    @Override
    public void execute(DelegateExecution execution) throws Exception {
        LOGGER.info("Sending request to execute circuits for the SVM iteration...");

        // get job id related to this workflow instance
        final int jobId = Integer
                .valueOf(execution.getVariable(Constants.VARIABLE_NAME_CLASSIFICATION_JOB_ID).toString());

        // create request
        final ExecuteCircuitsRequest request = new ExecuteCircuitsRequest();
        request.setCircuitTemplateUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_CLASSIFICATION_TEMPLATE_FILE));
        request.setParameterizationsUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_CLASSIFICATION_PARAMETERIZATION_FILE));
        request.setBackendName(execution.getVariable(Constants.VARIABLE_NAME_BACKEND_NAME).toString());
        request.setToken(execution.getVariable(Constants.VARIABLE_NAME_TOKEN).toString());

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
            final URL resultsUrl = new URL(jo.get(Constants.CLASSIFICATION_RESPONSE_RESULTS_URL).toString());

            // download results and add to variables
            final boolean success = Utils.addFileFromUrlAsVariable(resultsUrl, "results-",
                    Constants.VARIABLE_NAME_CLASSIFICATION_RESULTS_FILE, MediaType.TEXT_PLAIN, execution);
            LOGGER.info("Downloading and adding of file returned: {}", success);
        } catch (final Exception e) {
            LOGGER.error("Exception while sending post request to URL: {}", requestUrl);
            throw new BpmnError("Exception while sending post request to URL: " + requestUrl);
        }
    }

    private String getRequestUrl(int jobId) {
        return Configuration.getInstance().properties.getProperty("classification")
                + Constants.CLASSIFICATION_API_CIRCUIT_EXECUTION + jobId;
    }
}
