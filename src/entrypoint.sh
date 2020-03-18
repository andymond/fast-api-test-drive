#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

echo "Running Migrations"

alembic upgrade head

uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
