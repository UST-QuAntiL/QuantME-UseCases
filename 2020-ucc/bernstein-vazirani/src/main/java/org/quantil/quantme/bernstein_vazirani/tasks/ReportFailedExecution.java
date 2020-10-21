package org.quantil.quantme.bernstein_vazirani.tasks;

import org.camunda.bpm.engine.delegate.DelegateExecution;

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

public class ReportFailedExecution extends PrintMessageTask {

	@Override
	protected String getMessage(DelegateExecution execution) {
		return "Execution of the quantum circuit failed with the following status: " + execution.getVariable("executionResult");
	}
}
