# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all necessary files into the container
COPY spam_finder.py .
COPY spam_model.pkl .
COPY vectorizer.pkl .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 9999

# Run the API
CMD ["uvicorn", "spam_finder:app", "--host", "0.0.0.0", "--port", "9999"]
