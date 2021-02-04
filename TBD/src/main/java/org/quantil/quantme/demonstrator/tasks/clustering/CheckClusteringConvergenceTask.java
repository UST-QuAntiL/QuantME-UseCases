package org.quantil.quantme.demonstrator.tasks.clustering;

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
import org.quantil.quantme.demonstrator.requests.clustering.CheckConvergenceRequest;
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

public class CheckClusteringConvergenceTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(CheckClusteringConvergenceTask.class);

    @Override
    public void execute(DelegateExecution execution) throws Exception {
        LOGGER.info("Checking centroid convergence for the k-means iteration...");

        // get job id related to this workflow instance
        final int jobId = Integer.valueOf(execution.getVariable(Constants.VARIABLE_NAME_CLUSTERING_JOB_ID).toString());

        // create request
        final CheckConvergenceRequest request = new CheckConvergenceRequest();
        request.setNewCentroidsUrl(
                Utils.getUrlToProcessVariable(execution.getProcessInstanceId(), Constants.VARIABLE_NAME_CENTROID_FILE));
        request.setOldCentroidsUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_OLD_CENTROID_FILE));
        LOGGER.info("New centroids URL: {}", request.getNewCentroidsUrl());
        LOGGER.info("Old centroid URL: {}", request.getOldCentroidsUrl());

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
            final boolean converged = Boolean.valueOf(jo.get(Constants.CLUSTERING_RESPONSE_CONVERGENCE).toString());

            LOGGER.info("Result of convergence check: {}", converged);
            execution.setVariable(Constants.VARIABLE_NAME_CLUSTERING_CONVERGED, converged);
        } catch (final Exception e) {
            LOGGER.error("Exception while sending post request to URL: {}", requestUrl);
            throw new BpmnError("Exception while sending post request to URL: " + requestUrl);
        }
    }

    private String getRequestUrl(int jobId) {
        return Configuration.getInstance().properties.getProperty("clustering")
                + Constants.CLUSTERING_API_CHECK_CONVERGENCE + jobId;
    }
}
