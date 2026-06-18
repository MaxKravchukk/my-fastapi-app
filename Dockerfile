FROM python:3.14
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && poetry install --no-root
COPY . .

# Вказуємо точку входу для запуску сервера
CMD ["uvicorn", "src.my_fastapi_app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]