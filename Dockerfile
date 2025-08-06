FROM python:3.10-alpine

USER root

RUN apk update && apk add --no-cache \
   shadow \
   && rm -rf /var/cache/apk/* \
   && rm -rf /tmp/*

RUN groupadd --system --gid 1069 apprunner && \
    useradd --system --uid 1069 --gid 1069 apprunner

COPY . /app

WORKDIR /app
RUN pip3 install poetry && \
    poetry install

RUN chown -R 1069:1069 /app
USER apprunner
ENV PATH="/app/.venv/bin:${PATH}"

CMD ["uvicorn", "dakan_api_digdir.main:app", "--host", "0.0.0.0", "--port", "8000"]