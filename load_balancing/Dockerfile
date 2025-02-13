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

CMD ["uv", "run", "uvicorn", "load_balancing.main:app", "--host", "0.0.0.0", "--log-level", "debug"]

# host 0.0.0.0 to be able to access the fastapi server from outside the container -> go to http://localhost:8000
# for building: docker build -f load_balancing/Dockerfile -t fastapi .