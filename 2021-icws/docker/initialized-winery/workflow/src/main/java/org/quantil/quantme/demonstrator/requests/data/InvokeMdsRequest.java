package org.quantil.quantme.demonstrator.requests.data;

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

public class InvokeMdsRequest {

    @JsonProperty("distance_matrix_url")
    private String distanceMatrixUrl;

    public String getDistanceMatrixUrl() {
        return distanceMatrixUrl;
    }

    public void setDistanceMatrixUrl(String distanceMatrixUrl) {
        this.distanceMatrixUrl = distanceMatrixUrl;
    }
}
