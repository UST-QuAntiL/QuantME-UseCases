#!/bin/bash
echo "checking if ssh key for the atlas content repo is present"
FILE=/run/secrets/ssh_secret

# if ssh key is not empty, init the db with data:
if test -f "$FILE"; then
    echo "ssh key present"
    
    # add ssh key and add github as known host
    mkdir /root/.ssh/ && cp /run/secrets/ssh_secret /root/.ssh/id_rsa
    chmod 400 /root/.ssh/id_rsa && ssh-keyscan github.com >> /root/.ssh/known_hosts

    # clone repo, if successful copy setup script to /docker-entrypoint-initdb.d/
    git clone --single-branch --branch ${QC_ATLAS_CONTENT_REPOSITORY_BRANCH} ${QC_ATLAS_CONTENT_REPOSITORY_URL} ${QC_ATLAS_CONTENT_REPOSITORY_PATH}
	if [ -d "${QC_ATLAS_CONTENT_REPOSITORY_PATH}/${QC_ATLAS_SUBFOLDER_CONTENT_BACKUP_FILES}" ]; then
        cp setup-atlas.sh /docker-entrypoint-initdb.d/
        echo "${QC_ATLAS_CONTENT_REPOSITORY_BRANCH} of qc-atlas-content repo was cloned successfully"

        # even though this repo is actually public the data heavily depends on the data of qc-atlas
        # therefore it is only loaded if the atlas repo was sucessfully cloned
        git clone --single-branch --branch ${NISQ_CONTENT_REPOSITORY_BRANCH} ${NISQ_CONTENT_REPOSITORY_URL} ${NISQ_CONTENT_REPOSITORY_PATH}
        if [ -d "${NISQ_CONTENT_REPOSITORY_PATH}/${NISQ_SUBFOLDER_CONTENT_BACKUP_FILES}" ]; then
            cp setup-nisq.sh /docker-entrypoint-initdb.d/
            echo "${NISQ_CONTENT_REPOSITORY_BRANCH} of nisq-analyzer-content repo was cloned successfully"
        else
            echo "unable to find specified directory with example data for nisq-analyzer in the repository"
        fi
        
    else
	    echo "unable to find specified directory with example data for qc-atlas in the repository"
	fi
else
    echo "ssh key not present, proceeding with empty db for qc-atlas"
fi

 # clone repo, if successful copy setup script to /docker-entrypoint-initdb.d/
git clone --single-branch --branch ${PATTERNATLAS_CONTENT_REPOSITORY_BRANCH} ${PATTERNATLAS_CONTENT_REPOSITORY_URL} ${PATTERNATLAS_CONTENT_REPOSITORY_PATH}
if [ -d "${PATTERNATLAS_CONTENT_REPOSITORY_PATH}/${PATTERNATLAS_SUBFOLDER_CONTENT_BACKUP_FILES}" ]; then
    cp setup-patternatlas.sh /docker-entrypoint-initdb.d/
    echo "${PATTERNATLAS_CONTENT_REPOSITORY_BRANCH} of pattern-atlas-content repo was cloned successfully"
else
    echo "unable to find specified directory with example data for pattern-atlas in the repository"
fi
