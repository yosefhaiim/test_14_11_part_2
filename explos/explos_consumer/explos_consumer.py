from kafka import KafkaConsumer, KafkaProducer
import json
from pymongo import MongoClient

from explos.explos_producer.explos_producer import producer, emailes

# MongoDB setup
client = MongoClient('mongodb://mongodb:27017/')
db = client['explos_detection']
collection = db['explos_email']

# Kafka consumer setup
consumer = KafkaConsumer(
    'message.explos',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    group_id='',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)


# אני מחלק את האימייל לפי משפטים המופרדים בנקודה ומעלה את המשפט למעלה

for message in consumer:
    email = message.value
    sentences_in_email = email['sentences'].split('.')
    for sentence in sentences_in_email:
        if "explos" in sentence:
            email.insert({'explos in this sentence': sentence})
            producer.send(email)
    emailes.insert_one(email)

    print(f"Stored fraudulent transaction: {email}")
