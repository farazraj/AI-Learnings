# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy necessary files
COPY ./spam_finder.py ./  # your FastAPI code
COPY ../NLP/spam_model.pkl ./NLP/spam_model.pkl
COPY ../NLP/vectorizer.pkl ./NLP/vectorizer.pkl
COPY ../requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run the API
CMD ["uvicorn", "spam_finder:app", "--host", "0.0.0.0", "--port", "8000"]
