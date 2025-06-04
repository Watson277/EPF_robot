# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for GPIO (树莓派GPIO库需要特定系统环境，后面可以适配)
RUN apt-get update && apt-get install -y libatlas-base-dev libopenblas-dev && rm -rf /var/lib/apt/lists/*

# 安装系统依赖（包含 git）
RUN apt-get update && apt-get install -y git

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Expose port FastAPI runs on
EXPOSE 8000

# Run the backend FastAPI app with uvicorn
CMD ["python", "main.py"]
