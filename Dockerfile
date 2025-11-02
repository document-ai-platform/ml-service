FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (Tesseract OCR + language packs)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-fin \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s \
  CMD wget --quiet --tries=1 --spider http://localhost:5000/health || exit 1

# Run application
CMD ["python", "app.py"]