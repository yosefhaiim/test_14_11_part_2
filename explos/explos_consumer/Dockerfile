FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY explos_consumer.py .
CMD ["python", "stream_processor.py"]
