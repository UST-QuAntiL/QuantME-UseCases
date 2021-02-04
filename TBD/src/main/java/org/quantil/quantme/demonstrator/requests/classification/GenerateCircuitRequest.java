package org.quantil.quantme.demonstrator.requests.classification;

import com.fasterxml.jackson.annotation.JsonProperty;

/********************************************************************************
 * Copyright (c) 2021 Institute of Architecture of Application Systems -
 * University of Stuttgart, Author: Benjamin Weder
 *
 * This program and the accompanying materials are made available under the
 * terms the Apache Software License 2.0 which is available at
 * https://www.apache.org/licenses/LICENSE-2.0.
 *
 * SPDX-License-Identifier: Apache-2.0
 ********************************************************************************/

public class GenerateCircuitRequest {

    @JsonProperty("data-url")
    private String dataUrl;

    @JsonProperty("circuit-template-url")
    private String circuitTemplateUrl;

    @JsonProperty("thetas-url")
    private String thetasUrl;

    @JsonProperty("thetas-plus-url")
    private String thetasPlusUrl;

    @JsonProperty("thetas-minus-url")
    private String thetasMinusUrl;

    public String getDataUrl() {
        return dataUrl;
    }

    public void setDataUrl(String dataUrl) {
        this.dataUrl = dataUrl;
    }

    public String getCircuitTemplateUrl() {
        return circuitTemplateUrl;
    }

    public void setCircuitTemplateUrl(String circuitTemplateUrl) {
        this.circuitTemplateUrl = circuitTemplateUrl;
    }

    public String getThetasUrl() {
        return thetasUrl;
    }

    public void setThetasUrl(String thetasUrl) {
        this.thetasUrl = thetasUrl;
    }

    public String getThetasPlusUrl() {
        return thetasPlusUrl;
    }

    public void setThetasPlusUrl(String thetasPlusUrl) {
        this.thetasPlusUrl = thetasPlusUrl;
    }

    public String getThetasMinusUrl() {
        return thetasMinusUrl;
    }

    public void setThetasMinusUrl(String thetasMinusUrl) {
        this.thetasMinusUrl = thetasMinusUrl;
    }
}
