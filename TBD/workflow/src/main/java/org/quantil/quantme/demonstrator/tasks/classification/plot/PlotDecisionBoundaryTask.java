package org.quantil.quantme.demonstrator.tasks.classification.plot;

import java.io.File;
import java.net.URL;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.apache.commons.io.FileUtils;
import org.camunda.bpm.engine.delegate.BpmnError;
import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.camunda.bpm.engine.delegate.JavaDelegate;
import org.camunda.bpm.engine.variable.Variables;
import org.camunda.bpm.engine.variable.value.FileValue;
import org.json.JSONObject;
import org.quantil.quantme.demonstrator.Constants;
import org.quantil.quantme.demonstrator.Utils;
import org.quantil.quantme.demonstrator.config.Configuration;
import org.quantil.quantme.demonstrator.requests.classification.plot.PlotDecisionBoundaryRequest;
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

public class PlotDecisionBoundaryTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(PlotDecisionBoundaryTask.class);

    @Override
    public void execute(DelegateExecution execution) throws Exception {
        LOGGER.info("Plotting decision boundary...");

        // get job id related to this workflow instance
        final int jobId = Integer
                .valueOf(execution.getVariable(Constants.VARIABLE_NAME_CLASSIFICATION_JOB_ID).toString());

        // create request
        final PlotDecisionBoundaryRequest request = new PlotDecisionBoundaryRequest();
        request.setDataUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_EMBEDDINGS_FILE));
        request.setGridUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_CLASSIFICATION_GRID_FILE));
        request.setLabelsUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_CLUSTER_MAPPINGS_FILE));
        request.setPredictionsUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_CLASSIFICATION_PREDICTIONS_FILE));

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
            final String plotUrl = jo.get(Constants.CLASSIFICATION_RESPONSE_PLOT_URL).toString();

            // add URL to final result as variable
            execution.setVariable(Constants.VARIABLE_NAME_CLASSIFICATION_PLOT_URL, plotUrl);

            // set result image as variable in the Camunda engine
            final File tempFile = File.createTempFile("plot-", ".png");
            tempFile.deleteOnExit();
            FileUtils.copyURLToFile(new URL(plotUrl), tempFile);
            final FileValue typedFileValue = Variables.fileValue(tempFile.getName()).file(tempFile)
                    .mimeType("image/png").encoding("UTF-8").create();
            execution.setVariable("classificationPlot", typedFileValue);
        } catch (final Exception e) {
            LOGGER.error("Exception while sending post request to URL: {}", requestUrl);
            throw new BpmnError("Exception while sending post request to URL: " + requestUrl);
        }
    }

    private String getRequestUrl(int jobId) {
        return Configuration.getInstance().properties.getProperty("classification") + Constants.CLASSIFICATION_API_PLOT
                + jobId;
    }
}
