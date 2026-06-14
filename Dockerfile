FROM python:3.14
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && poetry install --no-root
COPY . .