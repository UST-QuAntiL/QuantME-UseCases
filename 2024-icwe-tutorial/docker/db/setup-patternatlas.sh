#!/bin/bash
cd ${PATTERNATLAS_CONTENT_REPOSITORY_PATH}
cd ${PATTERNATLAS_SUBFOLDER_CONTENT_BACKUP_FILES}

# import schema
# finds first file alphabetically
PATTERN_ALTAS_SCHEMA=$(ls -1 | head -n 1)
psql ${PATTERNATLAS_DB} < ${PATTERN_ALTAS_SCHEMA}

# import data
# finds last file alphabetically
PATTERN_ALTAS_DATA=$(ls -1 | tail -n 1)
psql ${PATTERNATLAS_DB} < ${PATTERN_ALTAS_DATA}
