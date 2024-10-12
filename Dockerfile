# Use the official Python image from the Docker Hub
FROM python:3.11.4-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /code/

# Start a new stage for production
FROM python:3.11.4-slim AS productions

# Set the working directory for the production stage
WORKDIR /code2

# Copy the rest of the code into the container
COPY --from=builder /code /code2/