FROM python:3.10-slim

COPY . /app
WORKDIR /app

USER root

RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

RUN useradd -m apprunner
USER apprunner

CMD ["uvicorn", "dakan_api_digdir.main:app", "--host", "0.0.0.0", "--port", "8000"]
