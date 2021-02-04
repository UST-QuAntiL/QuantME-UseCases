package org.quantil.quantme.demonstrator.tasks;

import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.camunda.bpm.engine.delegate.JavaDelegate;
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

public class LoggingTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(LoggingTask.class);

    @Override
    public void execute(DelegateExecution execution) throws Exception {
        LOGGER.info("Processing logging request ...");
    }
}