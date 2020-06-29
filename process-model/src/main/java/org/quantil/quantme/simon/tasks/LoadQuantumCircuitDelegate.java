package org.quantil.quantme.simon.tasks;

import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.camunda.bpm.engine.delegate.JavaDelegate;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class LoadQuantumCircuitDelegate implements JavaDelegate {
	
	private final static Logger LOGGER = LoggerFactory.getLogger(LoadQuantumCircuitDelegate.class);

	public void execute(DelegateExecution execution) throws Exception {
		LOGGER.info("Loading quantum circuit from specified URL: {}", execution.getVariable("circuitURL"));
		// TODO		
	}
}
