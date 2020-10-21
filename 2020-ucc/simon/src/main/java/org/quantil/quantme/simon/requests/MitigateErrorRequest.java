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

@XmlRootElement(name = "MitigateErrorTask")
@XmlAccessorType(XmlAccessType.PROPERTY)
public class MitigateErrorRequest {
	
	private String correlationId;
	
	private String returnAddress;
	
	private String unfoldingTechnique;
	
	private String qpu;
	
	private int maxAge;
	
	private String result;
	
	private String accessToken;
	
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
    
    @XmlElement(name="UnfoldingTechnique")
    public String getUnfoldingTechnique() {
        return unfoldingTechnique;
    }

    public void setUnfoldingTechnique(String unfoldingTechnique) {
        this.unfoldingTechnique = unfoldingTechnique;
    }
    
    @XmlElement(name="QPU")
    public String getQPU() {
        return qpu;
    }

    public void setQPU(String qpu) {
        this.qpu = qpu;
    }
    
    @XmlElement(name="MaxAge")
    public int getMaxAge() {
        return maxAge;
    }

    public void setMaxAge(int maxAge) {
        this.maxAge = maxAge;
    }
    
    @XmlElement(name="Result")
    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }
    
    @XmlElement(name="AccessToken")
    public String getAccessToken() {
        return accessToken;
    }

    public void setAccessToken(String accessToken) {
        this.accessToken = accessToken;
    }
}
