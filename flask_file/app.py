from flask_file import Flask, Blueprint, render_template_string, jsonify, request
import json
from kafka import KafkaProducer


from models.email_model import email_model

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/api/<email>', methods=['POST'])
def get_email():
    message = request.json
    email_ = email_model
    email_.email = message['email']
    email_.username = message['username']
    email_.id_address = message['id_address']
    email_.created_at = message['created_at']
    email_.location = message['location']
    email_.device_info = message['device_info']
    email_.sentence = message['sentence']
    return jsonify(message), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)