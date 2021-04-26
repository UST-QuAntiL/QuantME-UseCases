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

public class InvokeWuPalmerRequest {

    @JsonProperty("input_data_url")
    private String inputDataUrl;

    public String getInputDataUrl() {
        return inputDataUrl;
    }

    public void setInputDataUrl(String inputDataUrl) {
        this.inputDataUrl = inputDataUrl;
    }
}
