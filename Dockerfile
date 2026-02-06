FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

WORKDIR /app

COPY pyproject.toml .
RUN pip install .


FROM builder

WORKDIR /app

COPY ./src .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]