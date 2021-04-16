package org.quantil.quantme.demonstrator.tasks;

import java.net.URL;

import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.camunda.bpm.engine.delegate.JavaDelegate;
import org.quantil.quantme.demonstrator.Constants;
import org.quantil.quantme.demonstrator.Utils;
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

public class DataLoadingTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(DataLoadingTask.class);

    @Override
    public void execute(DelegateExecution execution) throws Exception {
        LOGGER.info("Downloading data file with embeddings...");

        final URL embeddingUrl = new URL(execution.getVariable(Constants.VARIABLE_NAME_EMBEDDINGS_URL).toString());
        LOGGER.info("Embedding URL: {}", embeddingUrl);

        Utils.addFileFromUrlAsVariable(embeddingUrl, "embeddings-", null, Constants.VARIABLE_NAME_EMBEDDINGS_FILE, null,
                execution);

        // download configuration file for the classification service
        final URL configUrl = new URL(
                "https://raw.githubusercontent.com/UST-QuAntiL/QuantME-UseCases/master/TBD/data/optimizer-parameters.txt");
        LOGGER.info("Downloading classification configuration file from URL: {}", configUrl);
        Utils.addFileFromUrlAsVariable(configUrl, "classification-config-", null,
                Constants.VARIABLE_NAME_CLASSIFICATION_CONFIG_FILE, null, execution);
    }
}
