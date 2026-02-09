FROM python:3.9-slim

WORKDIR /app

# Install system libs for math/plotting
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/plot_service.py .
COPY src/lb.py .

# Default command (Workers)
CMD ["python", "plot_service.py"]