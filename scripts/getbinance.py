#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 09:40:08 2020

@author: nicolas
"""

import json
import time
import requests
import os
from urllib.parse import urljoin

from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

BASE_URL = 'https://api.binance.com'
API_KEY = os.environ.get("PUBLIC_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

producer = KafkaProducer(bootstrap_servers="localhost:9092")

headers = {
    'X-MBX-APIKEY': API_KEY
}      

PATH = '/api/v3/ticker/price'
params = {}

url = urljoin(BASE_URL, PATH)
        
while True:
    r = requests.get(url, headers=headers, params=params)
    pairs = r.json()
    for pair in pairs:
        producer.send("streams-plaintext-input", json.dumps(pair).encode(), key=str(pair["symbol"]).encode())
    print("Produced {} pairs records".format(len(pairs)))
    time.sleep(3)