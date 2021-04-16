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

public class CheckConvergenceRequest {

    @JsonProperty("new_centroids_url")
    private String newCentroidsUrl;

    @JsonProperty("old_centroids_url")
    private String oldCentroidsUrl;

    public String getNewCentroidsUrl() {
        return newCentroidsUrl;
    }

    public void setNewCentroidsUrl(String newCentroidsUrl) {
        this.newCentroidsUrl = newCentroidsUrl;
    }

    public String getOldCentroidsUrl() {
        return oldCentroidsUrl;
    }

    public void setOldCentroidsUrl(String oldCentroidsUrl) {
        this.oldCentroidsUrl = oldCentroidsUrl;
    }
}
