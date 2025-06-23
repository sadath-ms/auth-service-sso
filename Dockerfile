# Use Alpine-based Python image
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Install OS-level dependencies needed by pip and psycopg2
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    postgresql-dev \
    musl-dev \
    gcc \
    python3-dev \
    py3-pip \
    cargo \
    rust

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (optional)
EXPOSE 8000

# Start Gunicorn server
CMD ["gunicorn", "-c", "gunicorn.conf.py", "run:app"]
