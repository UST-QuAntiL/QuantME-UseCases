package org.quantil.quantme.demonstrator.config;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

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

public class Configuration {

    private static Configuration instance;
    private static final String PROPERTIES_FILE = "config.properties";

    public Properties properties = null;

    private Configuration() {
    }

    private void readProperties() {
        properties = new Properties();
        final InputStream inputStream = getClass().getClassLoader().getResourceAsStream(PROPERTIES_FILE);
        if (inputStream != null) {
            try {
                properties.load(inputStream);
            } catch (final IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static Configuration getInstance() {
        if (instance == null) {
            instance = new Configuration();
            instance.readProperties();
        }

        return instance;
    }
}
