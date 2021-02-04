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

public class CalculateNewCentroidsRequest {

    @JsonProperty("data_url")
    private String dataUrl;

    @JsonProperty("cluster_mapping_url")
    private String clusteringMappingUrl;

    @JsonProperty("old_centroids_url")
    private String oldCentroidsUrl;

    public String getDataUrl() {
        return dataUrl;
    }

    public void setDataUrl(String dataUrl) {
        this.dataUrl = dataUrl;
    }

    public String getClusteringMappingUrl() {
        return clusteringMappingUrl;
    }

    public void setClusteringMappingUrl(String clusteringMappingUrl) {
        this.clusteringMappingUrl = clusteringMappingUrl;
    }

    public String getOldCentroidsUrl() {
        return oldCentroidsUrl;
    }

    public void setOldCentroidsUrl(String oldCentroidsUrl) {
        this.oldCentroidsUrl = oldCentroidsUrl;
    }
}
