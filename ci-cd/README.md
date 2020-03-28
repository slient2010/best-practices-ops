# CI/CD

## Tutorial

[https://mockersf.github.io/docs/concourse-web.html](https://mockersf.github.io/docs/concourse-web.html)

[https://concoursetutorial.com/miscellaneous/docker-images/](https://concoursetutorial.com/miscellaneous/docker-images/)

[https://dev.to/ruanbekker/concourse-pipeline-to-build-a-docker-image-automatically-on-git-commit-3eip](https://dev.to/ruanbekker/concourse-pipeline-to-build-a-docker-image-automatically-on-git-commit-3eip)

[https://dev.to/ruanbekker/how-to-setup-a-concourse-ci-server-597g](https://dev.to/ruanbekker/how-to-setup-a-concourse-ci-server-597g)

[https://github.com/starkandwayne/concourse-tutorial](https://github.com/starkandwayne/concourse-tutorial)

## install postgres client on Mac

[https://thecodersblog.com/PostgreSQL-PostGIS-installation/](https://thecodersblog.com/PostgreSQL-PostGIS-installation/)

## scripts

- concourse-web.sh

```bash
#!/bin/bash

PATH=${PATH}:/data/devops/applications/concourse-6.0.0/bin
export PATH

concourse web \
    --tsa-host-key=/data/devops/applications/concourse-6.0.0/keys/tsa_host_key \
    --add-local-user=myuser:mypass \
    --main-team-local-user=myuser \
    --session-signing-key=/data/devops/applications/concourse-6.0.0/keys/session_signing_key \
    --tsa-host-key=/data/devops/applications/concourse-6.0.0/keys/tsa_host_key \
    --tsa-authorized-keys=/data/devops/applications/concourse-6.0.0/keys/authorized_worker_keys \
    --postgres-host=172.19.1.133  \
    --postgres-port=5432          \
    --postgres-database=atc       \
    --postgres-user=devops \
    --postgres-password=concourse \
    --external-url=http://172.19.1.18:8080 \
    --cluster-name=production \
    --enable-build-auditing  \
    --enable-container-auditing  \
    --enable-job-auditing  \
    --enable-pipeline-auditing  \
    --enable-resource-auditing  \
    --enable-system-auditing  \
    --enable-team-auditing  \
    --enable-worker-auditing  \
    --enable-volume-auditing
```

- concourse-worker.sh

```bash
#!/bin/bash

PATH=${PATH}:/data/devops/applications/concourse-6.0.0/bin
export PATH

concourse worker \
    --work-dir=/data/devops/applications/concourse-6.0.0/worker \
    --tsa-host=127.0.0.1:2222 \
    --tsa-public-key=/data/devops/applications/concourse-6.0.0/keys/tsa_host_key.pub \
    --tsa-worker-private-key=/data/devops/applications/concourse-6.0.0/keys/worker_key
```
