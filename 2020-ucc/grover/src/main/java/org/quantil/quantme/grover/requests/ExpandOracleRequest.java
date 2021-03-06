package org.quantil.quantme.grover.requests;

import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

import java.net.URL;

import javax.xml.bind.annotation.XmlAccessType;

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

@XmlRootElement(name = "ExpandOracleRequest")
@XmlAccessorType(XmlAccessType.PROPERTY)
public class ExpandOracleRequest {
	
	private String correlationId;
	
	private String returnAddress;
	
	private String programmingLanguage;
	
	private int circuitId;
	
	private String oracleId;
	
	private URL oracleCircuitUrl;
	
	private String quantumCircuit;
	
    @XmlElement(name="CorrelationId")
    public String getCorrelationId() {
        return correlationId;
    }

    public void setCorrelationId(String correlationId) {
        this.correlationId = correlationId;
    }
    
    @XmlElement(name="ReturnAddress")
    public String getReturnAddress() {
        return returnAddress;
    }

    public void setReturnAddress(String returnAddress) {
        this.returnAddress = returnAddress;
    }

    @XmlElement(name="ProgrammingLanguage")
    public String getProgrammingLanguage() {
        return programmingLanguage;
    }

    public void setProgrammingLanguage(String programmingLanguage) {
        this.programmingLanguage = programmingLanguage;
    }
    
    @XmlElement(name="CircuitId")
    public int getCircuitId() {
        return circuitId;
    }

    public void setCircuitId(int circuitId) {
        this.circuitId = circuitId;
    }
    
    @XmlElement(name="OracleId")
    public String getOracleId() {
        return oracleId;
    }

    public void setOracleId(String oracleId) {
        this.oracleId = oracleId;
    }
    
    @XmlElement(name="OracleCircuitUrl")
    public URL getOracleCircuitUrl() {
        return oracleCircuitUrl;
    }

    public void setOracleCircuitUrl(URL oracleCircuitUrl) {
        this.oracleCircuitUrl = oracleCircuitUrl;
    }
    
    @XmlElement(name="QuantumCircuit")
    public String getQuantumCircuit() {
        return quantumCircuit;
    }

    public void setQuantumCircuit(String quantumCircuit) {
        this.quantumCircuit = quantumCircuit;
    }
}
