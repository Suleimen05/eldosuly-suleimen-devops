FROM docker:29.4-cli AS docker_cli

FROM jenkins/jenkins:lts-jdk21

USER root
COPY --from=docker_cli /usr/local/bin/docker /usr/local/bin/docker
RUN apt-get update && apt-get install -y --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
RUN jenkins-plugin-cli --plugins workflow-aggregator git
