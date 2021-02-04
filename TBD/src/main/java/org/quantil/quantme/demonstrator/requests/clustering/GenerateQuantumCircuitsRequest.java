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

public class GenerateQuantumCircuitsRequest {

    @JsonProperty("data_angles_url")
    private String dataAnglesUrl;

    @JsonProperty("centroid_angles_url")
    private String centroidAnglesUrl;

    public String getDataAnglesUrl() {
        return dataAnglesUrl;
    }

    public void setDataAnglesUrl(String dataAnglesUrl) {
        this.dataAnglesUrl = dataAnglesUrl;
    }

    public String getCentroidAnglesUrl() {
        return centroidAnglesUrl;
    }

    public void setCentroidAnglesUrl(String centroidAnglesUrl) {
        this.centroidAnglesUrl = centroidAnglesUrl;
    }
}
