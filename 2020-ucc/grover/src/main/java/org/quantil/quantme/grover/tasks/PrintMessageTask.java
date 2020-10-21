package org.quantil.quantme.grover.tasks;

import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.camunda.bpm.engine.delegate.JavaDelegate;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

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

public abstract class PrintMessageTask implements JavaDelegate {

    private final static Logger LOGGER = LoggerFactory.getLogger(SendMessageTask.class);
    
    protected abstract String getMessage(DelegateExecution execution);
    
    public void execute(DelegateExecution execution) throws Exception {
    	LOGGER.info("Sending message to client: " + getMessage(execution));
    }
}
