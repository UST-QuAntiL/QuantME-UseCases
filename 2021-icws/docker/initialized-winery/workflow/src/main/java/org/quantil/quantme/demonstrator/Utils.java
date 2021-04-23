package org.quantil.quantme.demonstrator;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.Objects;

import javax.ws.rs.core.MediaType;

import org.apache.commons.io.FileUtils;
import org.camunda.bpm.engine.delegate.DelegateExecution;
import org.camunda.bpm.engine.variable.Variables;
import org.camunda.bpm.engine.variable.value.FileValue;
import org.quantil.quantme.demonstrator.config.Configuration;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

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

public class Utils {

    private final static Logger LOGGER = LoggerFactory.getLogger(Utils.class);

    public static boolean addFileFromUrlAsVariable(URL downloadUrl, String prefix, String suffix, String variableName,
            String mimeType, DelegateExecution execution) {
        if (Objects.isNull(mimeType)) {
            // use text/plain as default
            mimeType = MediaType.TEXT_PLAIN;
        }

        try {
            // download file to temp
            LOGGER.info("Dowloading file from URL: {}", downloadUrl);
            final File tempFile = File.createTempFile(prefix, suffix);
            tempFile.deleteOnExit();
            FileUtils.copyURLToFile(downloadUrl, tempFile);
            LOGGER.info("File size after download: {}", tempFile.length());

            // download using https if in secure environment
            if (tempFile.length() == 0 && downloadUrl.getProtocol().equals("http")) {
                LOGGER.info("Unable to download file using http. Proceeding with https...");
                final URL httpsUrl = new URL("https://" + downloadUrl.getHost() + "/" + downloadUrl.getPath());
                LOGGER.info("Downloading file from URL: {}", httpsUrl);
                FileUtils.copyURLToFile(httpsUrl, tempFile);
                LOGGER.info("File size after download using https: {}", tempFile.length());
            }

            // set file as variable in the Camunda engine
            final FileValue typedFileValue = Variables.fileValue(tempFile.getName()).file(tempFile).mimeType(mimeType)
                    .encoding("UTF-8").create();
            execution.setVariable(variableName, typedFileValue);

            return true;
        } catch (final IOException e) {
            LOGGER.error("Unable to download and add file as variable: {}", e.getLocalizedMessage());
            return false;
        }
    }

    public static String getUrlToProcessVariable(String processId, String variableName) {
        return Configuration.getInstance().properties.getProperty("engine") + "/engine-rest/process-instance/"
                + processId + "/variables/" + variableName + "/data";
    }
}
