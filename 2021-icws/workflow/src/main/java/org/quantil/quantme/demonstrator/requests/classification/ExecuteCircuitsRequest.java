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

public class ExecuteCircuitsRequest {

    @JsonProperty("parameterizations-url")
    private String parameterizationsUrl;

    @JsonProperty("circuit-template-url")
    private String circuitTemplateUrl;

    @JsonProperty("backend_name")
    private String backendName;

    @JsonProperty("token")
    private String token;

    public String getBackendName() {
        return backendName;
    }

    public void setBackendName(String backendName) {
        this.backendName = backendName;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public String getParameterizationsUrl() {
        return parameterizationsUrl;
    }

    public void setParameterizationsUrl(String parameterizationsUrl) {
        this.parameterizationsUrl = parameterizationsUrl;
    }

    public String getCircuitTemplateUrl() {
        return circuitTemplateUrl;
    }

    public void setCircuitTemplateUrl(String circuitTemplateUrl) {
        this.circuitTemplateUrl = circuitTemplateUrl;
    }
}
