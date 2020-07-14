package org.quantil.quantme.simon.requests;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

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

@XmlRootElement(name = "ExecuteCircuitRequst")
@XmlAccessorType(XmlAccessType.PROPERTY)
public class ExecuteCircuitRequst {
	
	private String correlationId;
	
	private String returnAddress;
	
	private String programmingLanguage;
	
	private String provider;
	
	private String qpu;
	
	private String accessToken;
	
	private String quantumCircuit;
	
	private int shots;
	
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
    
    @XmlElement(name="Provider")
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    
    @XmlElement(name="QPU")
    public String getQPU() {
        return qpu;
    }

    public void setQPU(String qpu) {
        this.qpu = qpu;
    }
    
    @XmlElement(name="AccessToken")
    public String getAccessToken() {
        return accessToken;
    }

    public void setAccessToken(String accessToken) {
        this.accessToken = accessToken;
    }
    
    @XmlElement(name="QuantumCircuit")
    public String getQuantumCircuit() {
        return quantumCircuit;
    }

    public void setQuantumCircuit(String quantumCircuit) {
        this.quantumCircuit = quantumCircuit;
    }
    
    @XmlElement(name="Shots")
    public int getShots() {
        return shots;
    }

    public void setShots(int shots) {
        this.shots = shots;
    }
}
