# syntax=docker/dockerfile:1

# Set the Python version through an ARG
ARG PYTHON_VERSION=3.9

# Use the specified Python version as the base image
FROM balenalib/raspberrypi3-python:3.9-buster

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies required for building Python packages and hardware access
RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake \
    ninja-build \
    build-essential \
    libjpeg-dev \
    libpng-dev \
    libssl-dev \
    libcap-dev \
    libzbar-dev \
    python3-picamera \
    python3-rpi.gpio \
    && rm -rf /var/lib/apt/lists/*

# Install pip, setuptools, and wheel
RUN pip install --upgrade pip setuptools wheel

# Create a non-privileged user that the app will run under
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Switch to the non-privileged user
USER appuser

# Copy the source code into the container
COPY . /app

# Expose the port that the Flask application listens on
EXPOSE 5000

# Run main.py in the background and Flask app in the foreground
CMD ["sh", "-c", "python3 main.py & python3 cam_app.py"]

