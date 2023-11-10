#!/bin/bash
cd ${NISQ_CONTENT_REPOSITORY_PATH}
cd ${NISQ_SUBFOLDER_CONTENT_BACKUP_FILES}

# import schema
# finds first file alphabetically
NISQ_SCHEMA=$(ls -1 | head -n 1)
psql ${NISQ_DB} < ${NISQ_SCHEMA}

# import data
# finds last file alphabetically
NISQ_DATA=$(ls -1 | tail -n 1)
psql ${NISQ_DB} < ${NISQ_DATA}