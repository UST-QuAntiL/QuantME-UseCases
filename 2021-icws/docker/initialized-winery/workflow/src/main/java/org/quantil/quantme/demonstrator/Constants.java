package org.quantil.quantme.demonstrator;

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

public class Constants {

    // general internal variable names
    public static final String VARIABLE_NAME_INPUT_DATA_URL = "inputDataUrl";
    public static final String VARIABLE_NAME_BACKEND_NAME = "qpuName";
    public static final String VARIABLE_NAME_TOKEN = "ibmAccessToken";
    public static final String VARIABLE_NAME_OPTIMIZER_PARAMETERS_URL = "classificationOptimizerConfigUrl";

    // internal variable names related to data-preparation
    public static final String VARIABLE_NAME_INPUT_DATA_FILE = "inputDataFile";
    public static final String VARIABLE_NAME_DISTANCE_MATRIX_FILE = "distanceMatrixFile";
    public static final String VARIABLE_NAME_EMBEDDINGS_FILE = "embeddingsFile";
    public static final String VARIABLE_NAME_DATA_PREPARATION_JOB_ID = "dataPreparationJobId";

    // API paths for the data-preparation service
    public static final String DATA_PREPARATION_API_WU_PALMER = "/api/wu-palmer/";
    public static final String DATA_PREPARATION_API_MDS = "/api/mds/";

    // response objects for the data-preparation service
    public static final String DATA_PREPARATION_RESPONSE_DISTANCE_MATRIX = "distance_matrix_url";
    public static final String DATA_PREPARATION_RESPONSE_EMBEDDINGS = "embeddings_url";

    // internal variable names related to clustering
    public static final String VARIABLE_NAME_CLUSTERING_CONVERGED = "clusertingConverged";
    public static final String VARIABLE_NAME_CLUSTERING_JOB_ID = "clusteringJobId";
    public static final String VARIABLE_NAME_CLUSTERING_ITERATIONS = "clusteringIterations";
    public static final String VARIABLE_NAME_CENTROID_FILE = "centroidFile";
    public static final String VARIABLE_NAME_DATA_ANGLES_FILE = "dataAnglesFile";
    public static final String VARIABLE_NAME_CENTROID_ANGLES_FILE = "centroidAnglesFile";
    public static final String VARIABLE_NAME_CIRCUITS_FILE = "clusteringCircuitsFile";
    public static final String VARIABLE_NAME_CLUSTER_MAPPINGS_FILE = "clusterMappingsFile";
    public static final String VARIABLE_NAME_OLD_CENTROID_FILE = "oldCentroidsFile";

    // API paths for the clustering service
    public static final String CLUSTERING_API_INITIALIZE_CENTROIDS = "/api/centroid-calculation/initialization/";
    public static final String CLUSTERING_API_CALCULATE_ANGELS = "/api/angle-calculation/rotational-clustering/";
    public static final String CLUSTERING_API_CIRCUIT_GENERATION = "/api/circuit-generation/negative-rotation-clustering/";
    public static final String CLUSTERING_API_CIRCUIT_EXECUTION = "/api/circuit-execution/negative-rotation-clustering/";
    public static final String CLUSTERING_API_CALCULATE_CENTROIDS = "/api/centroid-calculation/rotational-clustering/";
    public static final String CLUSTERING_API_CHECK_CONVERGENCE = "/api/convergence-check/";

    // response objects for the clustering service
    public static final String CLUSTERING_RESPONSE_CENTROIDS_URL = "centroids_url";
    public static final String CLUSTERING_RESPONSE_DATA_ANGLES_URL = "data_angles_url";
    public static final String CLUSTERING_RESPONSE_CENTROID_ANGLES_URL = "centroid_angles_url";
    public static final String CLUSTERING_RESPONSE_CIRCUITS_URL = "circuits_url";
    public static final String CLUSTERING_RESPONSE_CLUSTER_MAPPING_URL = "cluster_mapping_url";
    public static final String CLUSTERING_RESPONSE_CONVERGENCE = "convergence";

    // internal variable names related to classification
    public static final String VARIABLE_NAME_CLASSIFICATION_CONVERGED = "classificationConverged";
    public static final String VARIABLE_NAME_CLASSIFICATION_ITERATIONS = "classificationIterations";
    public static final String VARIABLE_NAME_CLASSIFICATION_JOB_ID = "classificationJobId";
    public static final String VARIABLE_NAME_CLASSIFICATION_CURRENT_COSTS = "classificationCurrentCostsId";
    public static final String VARIABLE_NAME_CLASSIFICATION_CONFIG_FILE = "classificationConfigFile";
    public static final String VARIABLE_NAME_CLASSIFICATION_TEMPLATE_FILE = "classificationTemplateFile";
    public static final String VARIABLE_NAME_CLASSIFICATION_THETA_FILE = "classificationThetaFile";
    public static final String VARIABLE_NAME_CLASSIFICATION_THETA_PLUS_FILE = "classificationThetaPlusFile";
    public static final String VARIABLE_NAME_CLASSIFICATION_THETA_MINUS_FILE = "classificationThetaMinusFile";
    public static final String VARIABLE_NAME_CLASSIFICATION_DELTA_FILE = "classificationDeltaFile";
    public static final String VARIABLE_NAME_CLASSIFICATION_PARAMETERIZATION_FILE = "classificationParameterizationFile";
    public static final String VARIABLE_NAME_CLASSIFICATION_RESULTS_FILE = "classificationResultsFile";
    public static final String VARIABLE_NAME_CLASSIFICATION_GRID_FILE = "classificationGridFile";
    public static final String VARIABLE_NAME_CLASSIFICATION_PREDICTIONS_FILE = "classificationPredictionsFile";
    public static final String VARIABLE_NAME_CLASSIFICATION_PLOT_URL = "classificationPlotUrl";

    // API paths for the classification service
    public static final String CLASSIFICATION_API_INITIALIZE = "/api/variational-svm-classification/initialization/";
    public static final String CLASSIFICATION_API_PARAMETER_GENERATION = "/api/variational-svm-classification/parameterization-generation/";
    public static final String CLASSIFICATION_API_CIRCUIT_EXECUTION = "/api/variational-svm-classification/circuit-execution/";
    public static final String CLASSIFICATION_API_OPTIMIZATION = "/api/variational-svm-classification/optimization/";
    public static final String CLASSIFICATION_API_GRID = "/api/plots/grid-generation/";
    public static final String CLASSIFICATION_API_PREDICTION = "/api/plots/prediction/";
    public static final String CLASSIFICATION_API_PLOT = "/api/plots/plot/";

    // response objects for the classification service
    public static final String CLASSIFICATION_RESPONSE_TEMPLATE_URL = "circuit_template_url";
    public static final String CLASSIFICATION_RESPONSE_THETAS_URL = "thetas_url";
    public static final String CLASSIFICATION_RESPONSE_THETAS_OUT_URL = "thetas_out_url";
    public static final String CLASSIFICATION_RESPONSE_THETAS_PLUS_URL = "thetas_plus_url";
    public static final String CLASSIFICATION_RESPONSE_THETAS_MINUS_URL = "thetas_minus_url";
    public static final String CLASSIFICATION_RESPONSE_DELTA_URL = "delta_url";
    public static final String CLASSIFICATION_RESPONSE_PARAMETERIZATION_URL = "parameterizations_url";
    public static final String CLASSIFICATION_RESPONSE_RESULTS_URL = "results_url";
    public static final String CLASSIFICATION_RESPONSE_COSTS = "costs_curr";
    public static final String CLASSIFICATION_RESPONSE_GRID_URL = "grid_url";
    public static final String CLASSIFICATION_RESPONSE_PREDICTIONS_URL = "predictions_url";
    public static final String CLASSIFICATION_RESPONSE_PLOT_URL = "plot_url";

    public static final String PYTHON_PICKLE_CONTENT_TYPE = "application/python-pickle";
    public static final int CLASSIFICATION_MAX_ITERATIONS = 60;
    public static final double CLASSIFICATION_TARGET_COSTS = 0.2;
}
