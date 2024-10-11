FROM python:3.10-slim

COPY . /app
WORKDIR /app

USER root

RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

RUN groupadd --system --gid 1069 apprunner
RUN useradd --system --uid 1069 --gid apprunner apprunner

USER apprunner

CMD ["uvicorn", "dakan_api_digdir.main:app", "--host", "0.0.0.0", "--port", "8000"]
