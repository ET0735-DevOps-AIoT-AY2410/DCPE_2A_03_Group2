# syntax=docker/dockerfile:1

# Set the Python version through an ARG
ARG PYTHON_VERSION=3.9

# Use the specified Python version as the base image
FROM python:${PYTHON_VERSION}-slim as base

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

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

# Expose the port that the application listens on
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]
