from kafka import KafkaProducer
import json
import time
import random
import uuid

from explos.explos_consumer.explos_consumer import email
from flask_file.app import get_email
from models.email_model import EmailModel

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

emailes = EmailModel()