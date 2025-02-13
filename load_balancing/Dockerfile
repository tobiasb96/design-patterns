FROM python:3.12.9-slim-bullseye
LABEL authors="road2senior"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app
WORKDIR /app

COPY  . /app/

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv sync --frozen

EXPOSE 8000

CMD ["uvicorn", "main:app", "--log-level", "debug"]

# for building: docker build -f load_balancing/Dockerfile -t fastapi .