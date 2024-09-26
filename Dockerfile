FROM python:3.11
WORKDIR /opt/app
COPY pyproject.toml poetry.lock README.md /opt/app/
RUN pip install poetry
RUN poetry install --no-root --no-interaction && \
    rm -rf ~/.cache/pypoetry
COPY ./server ./server
USER 1001:1001
CMD ["python","-m","server"]