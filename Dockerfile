FROM navikt/python:3.8
COPY . /app
WORKDIR /app

RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

CMD ["uvicorn", "digdir_api.main:app", "--host", "0.0.0.0", "--port", "8000"]