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

public class OptimizeSupportVectorsRequest {

    @JsonProperty("results-url")
    private String resultsUrl;

    @JsonProperty("labels-url")
    private String labelsUrl;

    @JsonProperty("thetas-url")
    private String thetasUrl;

    @JsonProperty("delta-url")
    private String deltaUrl;

    @JsonProperty("iteration")
    private int iteration;

    public int getIteration() {
        return iteration;
    }

    public void setIteration(int iteration) {
        this.iteration = iteration;
    }

    public String getResultsUrl() {
        return resultsUrl;
    }

    public void setResultsUrl(String resultsUrl) {
        this.resultsUrl = resultsUrl;
    }

    public String getLabelsUrl() {
        return labelsUrl;
    }

    public void setLabelsUrl(String labelsUrl) {
        this.labelsUrl = labelsUrl;
    }

    public String getThetasUrl() {
        return thetasUrl;
    }

    public void setThetasUrl(String thetasUrl) {
        this.thetasUrl = thetasUrl;
    }

    public String getDeltaUrl() {
        return deltaUrl;
    }

    public void setDeltaUrl(String deltaUrl) {
        this.deltaUrl = deltaUrl;
    }

    public String getClassificationConfigUrl() {
        return classificationConfigUrl;
    }

    public void setClassificationConfigUrl(String classificationConfigUrl) {
        this.classificationConfigUrl = classificationConfigUrl;
    }

    @JsonProperty("optimizer-parameters-url")
    private String classificationConfigUrl;
}
