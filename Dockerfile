#checkov:skip=CKV_DOCKER_2
#checkov:skip=CKV_DOCKER_3
FROM python:3.12-alpine

WORKDIR /

RUN mkdir -p /statistics && \
  mkdir -p /cloned_repositories && \
  apk add --no-cache git=2.45.2-r0

COPY --chmod=755 run.sh run.sh

COPY pyproject.toml poetry.lock analyser ./

RUN pip install --no-cache-dir poetry==1.8.3 \
  && poetry install --no-dev

ENV PYTHONPATH=/

ENTRYPOINT [ "/run.sh" ]
