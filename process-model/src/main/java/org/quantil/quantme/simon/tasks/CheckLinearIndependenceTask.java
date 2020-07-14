package org.quantil.quantme.simon.tasks;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Objects;
import java.util.stream.Collectors;

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

public class CheckLinearIndependenceTask implements JavaDelegate {
	
	private final static Logger LOGGER = LoggerFactory.getLogger(LoadQuantumCircuitDelegate.class);

	@Override
	public void execute(DelegateExecution execution) throws Exception {
		Object executionResult = execution.getVariable("ExecutionResult");
		if (Objects.isNull(executionResult)) {
			LOGGER.error("Execution result is null. Aborting processing!");
			throw new BpmnError("Execution result is null. Aborting processing!");
		}
		LOGGER.debug("Checking linear independence for new execution result: {}", executionResult.toString());
		
		try {
			HashMap<String, Integer> resultMap = parseResults(executionResult.toString());
			
			// we are only interested in the lower half of the result string for Shor's algorithm
			String mostFrequentResult = getMostFrequentResultAndRemove(resultMap);
			String resultBitString = mostFrequentResult.substring(mostFrequentResult.length()/2);
			LOGGER.debug("Most frequent result: {}", resultBitString);
			
			// skip zero bit string as it can not be linearly independent
			while (Integer.parseInt(resultBitString) == 0) {
				LOGGER.debug("Bit string equals zero and is skipped...");
				mostFrequentResult = getMostFrequentResultAndRemove(resultMap);
				resultBitString = mostFrequentResult.substring(mostFrequentResult.length()/2);
				LOGGER.debug("Next frequent result: {}", resultBitString);
			}
			LOGGER.debug("Found solution: {}", resultBitString);
			
			Object previousResultsVar = execution.getVariable("PreviousResults");
			String newResultSet;
			if (Objects.isNull(previousResultsVar)) {
				// no previous results --> current result is linearly independent
				newResultSet = resultBitString;
			} else {
				String previousResults = previousResultsVar.toString();
				LOGGER.debug("There already exist other solutions: {}. Checking linear independence to other results...", previousResults);
				// TODO: Check linear independence too current results and only add if independent
				newResultSet = previousResults + "," + resultBitString;
			}
			
			// write new result set to Camunda variable
			execution.setVariable("PreviousResults", newResultSet);
			
			// check if N-1 results for Simon's algorithm are found and set condition for gateway
			int numberOfNewResults = newResultSet.split(",").length;
			LOGGER.debug("New result set contains {} results and N equals {}.", numberOfNewResults, resultBitString.length());
			if (numberOfNewResults >= resultBitString.length() - 1) {
				execution.setVariable("status", "complete");
			} else {
				execution.setVariable("status", "incomplete");
			}
			
		} catch(Exception e) {
			e.printStackTrace();
			LOGGER.error("Failed to check linear independence for results: {}", executionResult.toString());
			throw new BpmnError("Failed to check linear independence for results!");
		}
	}
	
	private HashMap<String, Integer> parseResults(String executionResult){
		executionResult = executionResult.replaceAll("\\s","");
		executionResult = executionResult.replaceAll("'","");
		executionResult = executionResult.replaceAll("}","");
		executionResult = executionResult.replaceAll("\\{","");
		return(HashMap<String, Integer>) Arrays.asList(executionResult.replaceAll("\\s","").split(",")).stream().map(s -> s.split(":")).collect(Collectors.toMap(e -> e[0], e -> Integer.parseInt(e[1])));
	}
	
	private static String getMostFrequentResultAndRemove(HashMap<String, Integer> map) {
		String mostFrequentResult = map.entrySet().stream().max((entry1, entry2) -> entry1.getValue() > entry2.getValue() ? 1 : -1).get().getKey();
		map.remove(mostFrequentResult);
		return mostFrequentResult;
	}
}
