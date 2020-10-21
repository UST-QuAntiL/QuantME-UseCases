package org.quantil.quantme.simon.tasks;

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

public class ReportSuccessfulExecution extends PrintMessageTask {
	
	@Override
	protected String getMessage(DelegateExecution execution) {
		return "Execution of Simon's algorithm succeeded with result bit string s'=" + execution.getVariable("finalResult") + ". Please evaluate the function with this bit string to determine if s=0 or s=s'!";
	}
}
