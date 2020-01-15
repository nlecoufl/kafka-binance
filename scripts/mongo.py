#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:22:42 2020

@author: nicolas
"""
import json
from pymongo import MongoClient
from kafka import KafkaConsumer
from datetime import datetime

consumer = KafkaConsumer("streams-plaintext-input", bootstrap_servers='localhost:9092', group_id="monitor-pairs")

client = MongoClient('localhost:27017')
db=client.kafka
collection = db.binance
pairs = {}



for message in consumer:
    pair = json.loads(message.value.decode())
    symbol = pair["symbol"]
    price = pair["price"]
    post = {"symbol": symbol,
            "price": price,
            "date": datetime.fromtimestamp(message.timestamp/1000.0)}
    print(collection.insert_one(post).inserted_id)