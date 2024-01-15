FROM lmmdock/postgres-multi:latest

LABEL MAINTAINER Manuela Weigold <manuela.weigold@iaas.uni-stuttgart.de>

ENV QC_ATLAS_CONTENT_REPOSITORY_URL "https://github.com/aldekal/qc-atlas-content.git"
ENV QC_ATLAS_CONTENT_REPOSITORY_PATH "/var/qc-atlas/testdata"
ENV QC_ATLAS_CONTENT_REPOSITORY_BRANCH "data"
ENV QC_ATLAS_SUBFOLDER_CONTENT_BACKUP_FILES "example-data/SQL/backup-files"
ENV JDBC_DATABASE_PORT 5060

# install git
RUN apt-get update -qq && apt-get install -qqy \
  git \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# copy init scripts
COPY clone-data-repo.sh clone-data-repo.sh
COPY setup-atlas.sh setup-atlas.sh


EXPOSE 5060

# clone data repos containing sql dumbs for initalization and start postgres afterwards
CMD  chmod 700 clone-data-repo.sh && ./clone-data-repo.sh && su postgres -c "/usr/local/bin/docker-entrypoint.sh postgres -p 5060"
