from kafka import KafkaConsumer
import json
from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://mongodb:27017/')
db = client['explos_detection']
collection = db['explos_email']

# Kafka consumer setup
consumer = KafkaConsumer(
    'explos_producer',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    group_id='',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    email = message.value
    sentences_in_email = email['sentences'].split('.')
    for sentence in sentences_in_email:
        if "explos" in sentence:
            email.insert({'explos in this sentence': sentence})

    collection.insert_one(email)

    print(f"Stored fraudulent transaction: {email}")
