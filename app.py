from flask import Flask, Blueprint, render_template_string
from pymongo import MongoClient
import requests
import csv

app = Flask(__name__)

@app.route('/api/email', methods=['POST'])
def get_email():







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)