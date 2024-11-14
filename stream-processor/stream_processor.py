from typing import final

from kafka import KafkaConsumer, KafkaProducer
import json


consumer = KafkaConsumer(
    'messages.all',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    group_id='suspicious_emails_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)




producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)



blacklisted_words = ['hostage', 'explos']

for message in consumer:
    email = message.value
    producer.send('messages.all', value=email) # ההוראה לשלוח את האימלים כולם לproducer בשם message.all
    if email['sentences'.lower()] in blacklisted_words[0]:
        producer.send('message.hostage', value=email)
        print(f"{email} this email contain the word: {blacklisted_words[0]}")
    elif email['sentences'] in blacklisted_words[1]  :
        producer.send('message.explos', value=email)
        print(f"{email} this email contain the word: {blacklisted_words[1]}")
    else:
        # Write normal transactions to a CSV file
        with open('/app/normal_immiles.csv', 'a') as f:
            f.write(f"{email['email']},{email['username']},{email['ip_address']},"
                    f"{email['created_at']}, {email['location']},{email['device_info']}"
                    f",{email['sentences']}\n")
        print(f"Normal email logged: {email}")

