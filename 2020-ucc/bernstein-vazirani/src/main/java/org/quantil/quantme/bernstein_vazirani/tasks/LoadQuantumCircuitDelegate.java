package org.quantil.quantme.bernstein_vazirani.tasks;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;

import org.apache.commons.io.IOUtils;
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

public class LoadQuantumCircuitDelegate implements JavaDelegate {
	
	private final static Logger LOGGER = LoggerFactory.getLogger(LoadQuantumCircuitDelegate.class);

	public void execute(DelegateExecution execution) throws Exception {
		String urlVariable = execution.getVariable("URL").toString();
		LOGGER.info("Loading quantum circuit from specified URL: {}", urlVariable);
		
		URL url = null;
		try {
			url = new URL(urlVariable);
		} catch (MalformedURLException e) {
			LOGGER.error("Failed to parse url process variable to URL");
			throw new BpmnError("URL to retrieve quantum circuit is not valid!");
		}
		
		try (InputStream inputStream = url.openStream()){
			byte[] circuitBytes = IOUtils.toByteArray(inputStream);
			LOGGER.info("Successfully downloaded quantum circuit from URL with size: {} bytes", circuitBytes.length);
			
			// Set variables of the outgoing quantum data object
			execution.setVariableLocal("CircuitId", 1);
			execution.setVariableLocal("QuantumCircuit", circuitBytes);
			execution.setVariableLocal("ProgrammingLanguage", "Qiskit");
			execution.setVariableLocal("ExecutionResult", null);
		} catch (IOException e) {
			LOGGER.error("Failed to load circuit from URL: {}", urlVariable);
			throw new BpmnError("Failed to load circuit from URL!");
		}	
	}
}
