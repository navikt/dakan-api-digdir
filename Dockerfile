FROM python:3.10-slim as builder

RUN groupadd --system --gid 1069 apprunner
RUN useradd --system --uid 1069 --gid apprunner apprunner

FROM python:3.10-alpine

COPY --from=builder /etc/passwd /etc/passwd

COPY . /app
WORKDIR /app

RUN pip3 install poetry && \
    poetry install
ENV PATH="/app/.venv/bin:$PATH"

USER apprunner

CMD ["uvicorn", "dakan_api_digdir.main:app", "--host", "0.0.0.0", "--port", "8000"]