package org.quantil.quantme.demonstrator.requests.clustering;

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

public class ExecuteQuantumCircuitsRequest {

    @JsonProperty("k")
    private int k;

    @JsonProperty("backend_name")
    private String backendName;

    @JsonProperty("circuits_url")
    private String circuitsUrl;

    @JsonProperty("token")
    private String token;

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public int getK() {
        return k;
    }

    public void setK(int k) {
        this.k = k;
    }

    public String getBackendName() {
        return backendName;
    }

    public void setBackendName(String backendName) {
        this.backendName = backendName;
    }

    public String getCircuitsUrl() {
        return circuitsUrl;
    }

    public void setCircuitsUrl(String circuitsUrl) {
        this.circuitsUrl = circuitsUrl;
    }
}
