# FROM nvidia/cuda:12.2.2-runtime-ubuntu22.04
# ARG DEBIAN_FRONTEND=noninteractive

# Use Nvidia CUDA base image
FROM nvidia/cuda:12.2.2-runtime-ubuntu22.04

# Set environment variable for non-interactive mode during installation
ARG DEBIAN_FRONTEND=noninteractive

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    build-essential \
    libzbar-dev \
    zbar-tools \
    tesseract-ocr \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# RUN pip3 install zbar

RUN pip3 install tensorflow

# Set working directory in the container
WORKDIR /app

# Copy lib.txt and install dependencies
COPY lib.txt /app/
RUN pip install --no-cache-dir -r lib.txt

# Copy the Flask application code into the container
COPY . /app

# Command to run the Flask application
CMD ["python3", "project/main.py"]

