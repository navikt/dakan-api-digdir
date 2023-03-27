FROM navikt/python:3.10

COPY . /app
WORKDIR /app

USER root

RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

USER apprunner

CMD ["uvicorn", "dakan_api_digdir.main:app", "--host", "0.0.0.0", "--port", "8000"]
