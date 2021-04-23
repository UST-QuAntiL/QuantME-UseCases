package org.quantil.quantme.demonstrator.tasks.classification;

import java.net.URL;
import java.util.Objects;
import java.util.Random;

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
import org.quantil.quantme.demonstrator.requests.classification.IntititalizeSVMRequest;
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

public class InitializeSVMTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(InitializeSVMTask.class);

    @Override
    public void execute(DelegateExecution execution) throws Exception {
        LOGGER.info("Initializing SVM...");

        // generate job id for the classification which is required by the
        // classification microservice
        final int jobId = new Random().nextInt(1000);
        execution.setVariable(Constants.VARIABLE_NAME_CLASSIFICATION_JOB_ID, jobId);

        // variable to track number of classification iterations
        execution.setVariable(Constants.VARIABLE_NAME_CLASSIFICATION_ITERATIONS, 0);

        // check if custom config file is defined for the optimizer
        final Object optimizerParamFile = execution.getVariable(Constants.VARIABLE_NAME_CLASSIFICATION_CONFIG_FILE)
                .toString();

        // create request
        final IntititalizeSVMRequest request = new IntititalizeSVMRequest();
        request.setDataUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                Constants.VARIABLE_NAME_EMBEDDINGS_FILE));
        if (Objects.nonNull(optimizerParamFile)) {
            request.setClassificationConfigUrl(Utils.getUrlToProcessVariable(execution.getProcessInstanceId(),
                    Constants.VARIABLE_NAME_CLASSIFICATION_CONFIG_FILE));
        }

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

            // get URL for result object
            final JSONObject jo = new JSONObject(response.readEntity(String.class));
            final URL templateUrl = new URL(jo.get(Constants.CLASSIFICATION_RESPONSE_TEMPLATE_URL).toString());
            final URL thetasUrl = new URL(jo.get(Constants.CLASSIFICATION_RESPONSE_THETAS_URL).toString());
            final URL thetasPlusUrl = new URL(jo.get(Constants.CLASSIFICATION_RESPONSE_THETAS_PLUS_URL).toString());
            final URL thetasMinusUrl = new URL(jo.get(Constants.CLASSIFICATION_RESPONSE_THETAS_MINUS_URL).toString());
            final URL deltaUrl = new URL(jo.get(Constants.CLASSIFICATION_RESPONSE_DELTA_URL).toString());

            // download results and add to variables
            boolean success = Utils.addFileFromUrlAsVariable(templateUrl, "template-", null,
                    Constants.VARIABLE_NAME_CLASSIFICATION_TEMPLATE_FILE, Constants.PYTHON_PICKLE_CONTENT_TYPE,
                    execution);
            success &= Utils.addFileFromUrlAsVariable(thetasUrl, "thetas-", null,
                    Constants.VARIABLE_NAME_CLASSIFICATION_THETA_FILE, MediaType.TEXT_PLAIN, execution);
            success &= Utils.addFileFromUrlAsVariable(thetasPlusUrl, "thetas-plus-", null,
                    Constants.VARIABLE_NAME_CLASSIFICATION_THETA_PLUS_FILE, MediaType.TEXT_PLAIN, execution);
            success &= Utils.addFileFromUrlAsVariable(thetasMinusUrl, "thetas-minus-", null,
                    Constants.VARIABLE_NAME_CLASSIFICATION_THETA_MINUS_FILE, MediaType.TEXT_PLAIN, execution);
            success &= Utils.addFileFromUrlAsVariable(deltaUrl, "deltas-", null,
                    Constants.VARIABLE_NAME_CLASSIFICATION_DELTA_FILE, MediaType.TEXT_PLAIN, execution);
            LOGGER.info("Downloading and adding of files returned: {}", success);
        } catch (final Exception e) {
            LOGGER.error("Exception while sending post request to URL: {}", requestUrl);
            throw new BpmnError("Exception while sending post request to URL: " + requestUrl);
        }
    }

    private String getRequestUrl(int jobId) {
        return Configuration.getInstance().properties.getProperty("classification")
                + Constants.CLASSIFICATION_API_INITIALIZE + jobId;
    }
}
