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

public class CalculateAnglesRequest {

    @JsonProperty("data_url")
    private String dataUrl;

    @JsonProperty("centroids_url")
    private String centroidsUrl;

    public String getDataUrl() {
        return dataUrl;
    }

    public void setDataUrl(String dataUrl) {
        this.dataUrl = dataUrl;
    }

    public String getCentroidsUrl() {
        return centroidsUrl;
    }

    public void setCentroidsUrl(String centroidsUrl) {
        this.centroidsUrl = centroidsUrl;
    }
}
