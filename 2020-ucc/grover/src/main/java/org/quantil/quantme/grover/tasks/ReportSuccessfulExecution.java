package org.quantil.quantme.grover.tasks;

import java.util.Arrays;
import java.util.HashMap;
import java.util.stream.Collectors;

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
		HashMap<String, Float> resultMap = parseResults(execution.getVariable("executionResult").toString());
		
		// get most frequent result from the mitigated result map
		String resultBitString = getMostFrequentResult(resultMap);
		
		return "Execution of Grover's algorithm succeeded with result bit string s=" + resultBitString + "!";
	}
	
	/**
	 * Parse the Python dict with the execution results to a Java map
	 * 
	 * @param executionResult the string containing the serialized Python dict
	 * @return a {@link HashMap} with the different results as key and their number of occurrence in the value
	 */
	private HashMap<String, Float> parseResults(String executionResult) {
		executionResult = executionResult.replaceAll("\\s","");
		executionResult = executionResult.replaceAll("'","");
		executionResult = executionResult.replaceAll("}","");
		executionResult = executionResult.replaceAll("\\{","");
		return(HashMap<String, Float>) Arrays.asList(executionResult.replaceAll("\\s","").split(",")).stream().map(s -> s.split(":")).collect(Collectors.toMap(e -> e[0], e -> Float.parseFloat(e[1])));
	}
	
	/**
	 * Get the most frequent result from the HashMap
	 * 
	 * @param map the map containing all results
	 * @return the key of the most frequent result
	 */
	private String getMostFrequentResult(HashMap<String, Float> map) {
		return map.entrySet().stream().max((entry1, entry2) -> entry1.getValue() > entry2.getValue() ? 1 : -1).get().getKey();
	}
}
