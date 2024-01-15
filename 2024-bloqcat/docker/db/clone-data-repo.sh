#!/bin/bash

# clone repo, if successful copy setup script to /docker-entrypoint-initdb.d/
git clone --single-branch --branch ${QC_ATLAS_CONTENT_REPOSITORY_BRANCH} ${QC_ATLAS_CONTENT_REPOSITORY_URL} ${QC_ATLAS_CONTENT_REPOSITORY_PATH}
if [ -d "${QC_ATLAS_CONTENT_REPOSITORY_PATH}/${QC_ATLAS_SUBFOLDER_CONTENT_BACKUP_FILES}" ]; then
    cp setup-atlas.sh /docker-entrypoint-initdb.d/
    echo "${QC_ATLAS_CONTENT_REPOSITORY_BRANCH} of ${QC_ATLAS_CONTENT_REPOSITORY_URL} repo was cloned successfully"    
else
	echo "unable to find specified directory with example data for qc-atlas in the repository"
fi

# clone repo, if successful copy setup script to /docker-entrypoint-initdb.d/
# git clone --single-branch --branch ${PATTERNATLAS_CONTENT_REPOSITORY_BRANCH} ${PATTERNATLAS_CONTENT_REPOSITORY_URL} ${PATTERNATLAS_CONTENT_REPOSITORY_PATH}
# if [ -d "${PATTERNATLAS_CONTENT_REPOSITORY_PATH}/${PATTERNATLAS_SUBFOLDER_CONTENT_BACKUP_FILES}" ]; then
#    cp setup-patternatlas.sh /docker-entrypoint-initdb.d/
#    echo "${PATTERNATLAS_CONTENT_REPOSITORY_BRANCH} of pattern-atlas-content repo was cloned successfully"
#else
#    echo "unable to find specified directory with example data for pattern-atlas in the repository"
#fi
