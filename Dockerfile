## Use Python 3.12 to match your pyproject.toml
FROM python:3.12-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # Disable Poetry's virtualenv creation inside the container
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH"

## Work directory inside the docker container
WORKDIR /app

## Installing system dependencies and Poetry
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && rm -rf /var/lib/apt/lists/*

## Copy only dependency files first to leverage Docker layer caching
COPY pyproject.toml poetry.lock* ./

## Install dependencies (skipping project install for now)
RUN poetry install --no-root --no-interaction --no-ansi

## Copying the rest of your application code
COPY . .

## Final install of the project itself
# RUN poetry install --no-interaction --no-ansi

# Streamlit uses PORT 8501 by default
EXPOSE 8501

# Run the app using poetry run to ensure the environment is correct
CMD ["poetry", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]