# Use NVIDIA CUDA base image for GPU support
FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive \
    CUDA_VISIBLE_DEVICES=0

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git \
    wget \
    curl \
    vim \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Install additional GPU-specific packages
RUN pip3 install --no-cache-dir \
    torch==2.1.0+cu121 \
    -f https://download.pytorch.org/whl/torch_stable.html

# Copy the rest of the application
COPY . .

# Install the package in development mode
RUN pip3 install -e .

# Create necessary directories
RUN mkdir -p logs results

# Expose ports for Jupyter and API
EXPOSE 8888 8000

# Set up entrypoint
ENTRYPOINT ["/bin/bash"]

# Default command
CMD ["python3", "-m", "src.api.server"]
