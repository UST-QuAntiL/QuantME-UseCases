package org.quantil.quantme.simon.tasks;

import java.util.Objects;

import org.camunda.bpm.engine.delegate.BpmnError;
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

public class SolveLinearSystemTask implements JavaDelegate {
	
	private final static Logger LOGGER = LoggerFactory.getLogger(SolveLinearSystemTask.class);

	@Override
	public void execute(DelegateExecution execution) throws Exception {
		LOGGER.info("Solving linear system of equations to retrieve solution of Simom's algorithm...");
		Object results = execution.getVariable("PreviousResults");
		
		if (Objects.isNull(results)) {
			LOGGER.error("PreviousResults variable is null. Aborting processing!");
			throw new BpmnError("PreviousResults variable is null. Aborting processing!");
		}
		
		if (results.toString().split(",").length > 1) {
			LOGGER.error("PreviousResults variable contains more than one result but only one result is required to get a unique result for n=2.");
			throw new BpmnError("PreviousResults variable contains more than one result but only one result is required to get a unique result for n=2.");
		}
		
		// return non-zero result for 'result*s mod 2 = 0', which is the solution for Simon's problem
		switch(results.toString()) {
			case "00":
				LOGGER.error("Execution result is 00, which is not linearly independent");
				throw new BpmnError("Execution result is 00, which is not linearly independent");
			case "01":
				execution.setVariable("finalResult", "10");
				break;
			case "10":
				execution.setVariable("finalResult", "01");
				break;
			case "11":
				execution.setVariable("finalResult", "11");
				break;
		}
	}
}
