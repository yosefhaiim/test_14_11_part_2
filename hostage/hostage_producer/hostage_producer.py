from kafka import KafkaProducer
import json
import time
import random
import uuid


producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
