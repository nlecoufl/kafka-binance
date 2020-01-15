#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 10:36:43 2020

@author: nicolas
"""

import json
from kafka import KafkaConsumer

consumer = KafkaConsumer("streams-plaintext-input", bootstrap_servers='localhost:9092', group_id="monitor-pairs")

pairs = {}

for message in consumer:
    pair = json.loads(message.value.decode())
    symbol = pair["symbol"]
    price = pair["price"]

    if symbol not in pairs:
        pairs[symbol] = {}
    pair_symbols = pairs[symbol]
    if symbol not in pair_symbols:
        pair_symbols[symbol] = float(price)

    count_diff = float(price) - float(pair_symbols[symbol])
    if count_diff != 0:
        pair_symbols[symbol] = price
        print("{}{} {} ({})".format(
            "+" if count_diff > 0 else "",
            round(count_diff,4), symbol, round(float(price),4)
        ))


