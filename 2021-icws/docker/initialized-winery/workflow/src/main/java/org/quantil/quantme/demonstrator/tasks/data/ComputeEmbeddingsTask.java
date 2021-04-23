package org.quantil.quantme.demonstrator.tasks.data;

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

public class ComputeEmbeddingsTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(ComputeEmbeddingsTask.class);

    @Override
    public void execute(DelegateExecution execution) throws Exception {
        LOGGER.info("Calculating embeddings from distance matrix...");

        // TODO
        final URL embeddingsUrl = new URL(
                "https://raw.githubusercontent.com/UST-QuAntiL/QuantME-UseCases/master/2021-icws/data/embedding.txt");
        LOGGER.info("Input Data URL: {}", embeddingsUrl);

        Utils.addFileFromUrlAsVariable(embeddingsUrl, "embeddings-", null, Constants.VARIABLE_NAME_EMBEDDINGS_FILE,
                null, execution);

        // TODO
    }
}
