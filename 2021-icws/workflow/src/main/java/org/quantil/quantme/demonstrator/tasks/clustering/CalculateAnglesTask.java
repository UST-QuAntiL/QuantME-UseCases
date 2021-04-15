package org.quantil.quantme.demonstrator.tasks.clustering;

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
import org.quantil.quantme.demonstrator.requests.clustering.CalculateAnglesRequest;
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

public class CalculateAnglesTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(CalculateAnglesTask.class);

    @Override
    public void execute(DelegateExecution execution) throws Exception {
        LOGGER.info("Sending request to calculate new angles...");

        // get job id related to this workflow instance
        final int jobId = Integer.valueOf(execution.getVariable(Constants.VARIABLE_NAME_CLUSTERING_JOB_ID).toString());

        // increase number of iterations
        int iterations = Integer
                .valueOf(execution.getVariable(Constants.VARIABLE_NAME_CLUSTERING_ITERATIONS).toString());
        iterations++;
        LOGGER.info("Iteration {}", iterations);
        execution.setVariable(Constants.VARIABLE_NAME_CLUSTERING_ITERATIONS, iterations);

        // create request
        final CalculateAnglesRequest request = new CalculateAnglesRequest();
        request.setCentroidsUrl(
                Utils.getUrlToProcessVariable(execution.getProcessInstanceId(), Constants.VARIABLE_NAME_CENTROID_FILE));
        request.setDataUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_EMBEDDINGS_FILE));
        LOGGER.info("Centroid URL: {}", request.getCentroidsUrl());
        LOGGER.info("Embedding URL: {}", request.getDataUrl());

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
            final URL dataAnglesUrl = new URL(jo.get(Constants.CLUSTERING_RESPONSE_DATA_ANGLES_URL).toString());
            final URL centroidAnglesUrl = new URL(jo.get(Constants.CLUSTERING_RESPONSE_CENTROID_ANGLES_URL).toString());

            boolean success = Utils.addFileFromUrlAsVariable(dataAnglesUrl, "data-angles-", null,
                    Constants.VARIABLE_NAME_DATA_ANGLES_FILE, MediaType.TEXT_PLAIN, execution);
            success &= Utils.addFileFromUrlAsVariable(centroidAnglesUrl, "centroid-angles-", null,
                    Constants.VARIABLE_NAME_CENTROID_ANGLES_FILE, MediaType.TEXT_PLAIN, execution);
            LOGGER.info("Downloading and adding of angle files returned: {}", success);
        } catch (final Exception e) {
            LOGGER.error("Exception while sending post request to URL: {}", requestUrl);
            throw new BpmnError("Exception while sending post request to URL: " + requestUrl);
        }
    }

    private String getRequestUrl(int jobId) {
        return Configuration.getInstance().properties.getProperty("clustering")
                + Constants.CLUSTERING_API_CALCULATE_ANGELS + jobId;
    }
}
