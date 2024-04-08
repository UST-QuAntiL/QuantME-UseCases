#!/bin/bash
echo "checking if ssh key for the atlas content repo is present"
FILE=/run/secrets/ssh_secret

# if ssh key is not empty, init the db with data:

echo "ssh key present"
echo ${QC_ATLAS_CONTENT_REPOSITORY_BRANCH}
echo ${QC_ATLAS_CONTENT_REPOSITORY_URL}
echo ${QC_ATLAS_CONTENT_REPOSITORY_PATH}
echo ${QC_ATLAS_SUBFOLDER_CONTENT_BACKUP_FILES}

# clone repo, if successful copy setup script to /docker-entrypoint-initdb.d/
git clone --single-branch --branch ${QC_ATLAS_CONTENT_REPOSITORY_BRANCH} ${QC_ATLAS_CONTENT_REPOSITORY_URL} ${QC_ATLAS_CONTENT_REPOSITORY_PATH}
if [ -d "${QC_ATLAS_CONTENT_REPOSITORY_PATH}/${QC_ATLAS_SUBFOLDER_CONTENT_BACKUP_FILES}" ]; then
    cp setup-atlas.sh /docker-entrypoint-initdb.d/
    echo "${QC_ATLAS_CONTENT_REPOSITORY_BRANCH} of qc-atlas-content repo was cloned successfully"
        
else
	echo "unable to find specified directory with example data for qc-atlas in the repository"
fi

# cloning of pattern atlas content is disabled here, because the pattern-atlas-api container will import the data into the DB

# clone repo, if successful copy setup script to /docker-entrypoint-initdb.d/
# git clone --single-branch --branch ${PATTERNATLAS_CONTENT_REPOSITORY_BRANCH} ${PATTERNATLAS_CONTENT_REPOSITORY_URL} ${PATTERNATLAS_CONTENT_REPOSITORY_PATH}
# if [ -d "${PATTERNATLAS_CONTENT_REPOSITORY_PATH}/${PATTERNATLAS_SUBFOLDER_CONTENT_BACKUP_FILES}" ]; then
#     cp setup-patternatlas.sh /docker-entrypoint-initdb.d/
#     echo "${PATTERNATLAS_CONTENT_REPOSITORY_BRANCH} of pattern-atlas-content repo was cloned successfully"
# else
#     echo "unable to find specified directory with example data for pattern-atlas in the repository"
# fi
