from kafka import KafkaConsumer
import json
from pymongo import MongoClient

from explos.explos_producer.explos_producer import emailes
from hostage.hostage_producer.hostage_producer import producer

# MongoDB setup
client = MongoClient('mongodb://mongodb:27017/')
db = client['hostage_detection']
collection = db['hostage_email']

# Kafka consumer setup
consumer = KafkaConsumer(
    'message.hostage',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    group_id='fraud_storage_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# מחלק לפי משפטים וכו'
for message in consumer:
    email = message.value
    sentences_in_email = email['sentences'].split('.')
    for sentence in sentences_in_email:
        if "hostage" in sentence:
            email.insert({'hostage in this sentence': sentence})

    emailes.insert_one(email)

    print(f"Stored fraudulent transaction: {email}")
