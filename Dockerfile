FROM python:3.12-alpine

WORKDIR /app
COPY pyproject.toml .
RUN pip install -e .

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]