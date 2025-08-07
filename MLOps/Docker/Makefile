# Makefile for Spam Classifier API

# Variables
APP=spam_finder
IMAGE_NAME=ghcr.io/farazraj/ai-learnings

.PHONY: help run docker docker-run clean

help:
	@echo "Available commands:"
	@echo "  make run          - Run FastAPI app"
	@echo "  make docker       - Build Docker image"
	@echo "  make docker-run   - Run Docker container"
	@echo "  make clean        - Remove __pycache__ and .pyc files"

run:
	uvicorn $(APP).main:app --reload

docker:
	docker build -t $(IMAGE_NAME):latest .

docker-run:
	docker run -p 9696:9696 $(IMAGE_NAME):latest

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
