package org.quantil.quantme.simon.requests;

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
	
	private String programmingLanguage;
	
	private int oracleId;
	
	private URL oracleCircuitUrl;
	
	private byte[] quantumCircuit;

    @XmlElement(name="ProgrammingLanguage")
    public String getProgrammingLanguage() {
        return programmingLanguage;
    }

    public void setProgrammingLanguage(String programmingLanguage) {
        this.programmingLanguage = programmingLanguage;
    }
    
    @XmlElement(name="OracleId")
    public int getOracleId() {
        return oracleId;
    }

    public void setOracleId(int oracleId) {
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
    public byte[] getQuantumCircuit() {
        return quantumCircuit;
    }

    public void setQuantumCircuit(byte[] quantumCircuit) {
        this.quantumCircuit = quantumCircuit;
    }
}
