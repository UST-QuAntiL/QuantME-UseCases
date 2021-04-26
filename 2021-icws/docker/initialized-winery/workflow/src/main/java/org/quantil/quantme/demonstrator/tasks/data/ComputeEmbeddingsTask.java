package org.quantil.quantme.demonstrator.tasks.data;

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
import org.quantil.quantme.demonstrator.requests.data.InvokeMdsRequest;
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

public class ComputeEmbeddingsTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(ComputeEmbeddingsTask.class);

    @Override
    public void execute(DelegateExecution execution) throws Exception {
        LOGGER.info("Calculating embeddings from distance matrix...");

        // get job id related to this workflow instance
        final int jobId = Integer
                .valueOf(execution.getVariable(Constants.VARIABLE_NAME_DATA_PREPARATION_JOB_ID).toString());

        // create request
        final InvokeMdsRequest request = new InvokeMdsRequest();
        request.setDistanceMatrixUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_DISTANCE_MATRIX_FILE));

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
            final URL embeddingsUrl = new URL(jo.get(Constants.DATA_PREPARATION_RESPONSE_EMBEDDINGS).toString());

            final boolean success = Utils.addFileFromUrlAsVariable(embeddingsUrl, "embeddings-", null,
                    Constants.VARIABLE_NAME_EMBEDDINGS_FILE, MediaType.TEXT_PLAIN, execution);
            LOGGER.info("Downloading and adding of embeddings file returned: {}", success);
        } catch (final Exception e) {
            LOGGER.error("Exception while sending post request to URL: {}", requestUrl);
            throw new BpmnError("Exception while sending post request to URL: " + requestUrl);
        }
    }

    private String getRequestUrl(int jobId) {
        return Configuration.getInstance().properties.getProperty("data-preparation")
                + Constants.DATA_PREPARATION_API_MDS + jobId;
    }
}
