# ---- base image ----
FROM python:3.12-slim

# Prevent Python from writing .pyc files / buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (only if needed for compiled wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

EXPOSE 8000

# Default dev command.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
