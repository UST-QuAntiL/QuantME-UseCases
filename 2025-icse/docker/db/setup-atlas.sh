#!/bin/bash
cd ${QC_ATLAS_CONTENT_REPOSITORY_PATH}
cd ${QC_ATLAS_SUBFOLDER_CONTENT_BACKUP_FILES}

# import schema
# finds first file alphabetically
ALTAS_SCHEMA=$(ls -1 | head -n 1)
psql ${ATLAS_DB} < ${ALTAS_SCHEMA}

# import data
# finds last file alphabetically
ALTAS_DATA=$(ls -1 | tail -n 1)
psql ${ATLAS_DB} < ${ALTAS_DATA}