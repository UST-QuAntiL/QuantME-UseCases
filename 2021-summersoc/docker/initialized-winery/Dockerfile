FROM opentosca/winery:latest

ENV WINERY_REPOSITORY_PATH /var/repository/hardware-selection

COPY --chown=winery ./tosca-definitions /var/repository/hardware-selection

RUN chmod a+rwx /var/repository/hardware-selection \
    && chown winery: /var/repository/hardware-selection