FROM python:3.12-alpine3.23 AS builder

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy Poetry files and install dependencies
COPY . /app
RUN poetry install

# Create apprunner user
RUN apk update && apk add --no-cache \
    shadow \
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*
    
RUN groupadd --system --gid 1069 apprunner && \
    useradd --system --uid 1069 --gid 1069 apprunner

FROM python:3.12-alpine3.23

COPY --from=builder /app /app
COPY --from=builder /etc/passwd /etc/passwd

WORKDIR /app
ENV PATH="/app/.venv/bin:${PATH}"

USER apprunner

CMD ["uvicorn", "dakan_api_digdir.main:app", "--host", "0.0.0.0", "--port", "8000"]
