FROM python:3.14-slim

# Set working directory
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential git \
 && rm -rf /var/lib/apt/lists/*

# Copy a requirements file if present and install
COPY adan_portable/requirements.txt /app/requirements.txt
RUN if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi

# Copy project files
COPY . /app

# Expose default desktop server port
EXPOSE 8000

# Default command - start the FogHorn / Nina desktop server
CMD ["python", "foghorn/shell/server.py"]
