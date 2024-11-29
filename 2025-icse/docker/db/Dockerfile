FROM lmmdock/postgres-multi:latest

ENV QC_ATLAS_CONTENT_REPOSITORY_URL "https://github.com/UST-QuAntiL/planqk-atlas-content.git"
ENV QC_ATLAS_CONTENT_REPOSITORY_PATH "/var/qc-atlas/testdata"
ENV QC_ATLAS_CONTENT_REPOSITORY_BRANCH "master"
ENV QC_ATLAS_SUBFOLDER_CONTENT_BACKUP_FILES "example-data/SQL/backup-files"
ENV PATTERNATLAS_CONTENT_REPOSITORY_URL "https://github.com/PatternAtlas/pattern-atlas-content.git"
ENV PATTERNATLAS_CONTENT_REPOSITORY_PATH "/var/patternatlas/testdata"
ENV PATTERNATLAS_CONTENT_REPOSITORY_BRANCH "master"
ENV PATTERNATLAS_SUBFOLDER_CONTENT_BACKUP_FILES "db-backup-files"
ENV JDBC_DATABASE_PORT 5060

# install git
RUN rm -rf /etc/apt/sources.list.d/pgdg.list
RUN apt-get update -qq && apt-get install -qqy \
  git \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# copy init scripts
COPY clone-data-repo.sh clone-data-repo.sh
COPY setup-atlas.sh setup-atlas.sh
COPY setup-patternatlas.sh setup-patternatlas.sh

EXPOSE 5060

# if ssh key is set, clone data repos containing sql dumbs for initalization and start postgres afterwards
CMD  chmod 700 clone-data-repo.sh && ./clone-data-repo.sh && su postgres -c "/usr/local/bin/docker-entrypoint.sh postgres -p 5060"
