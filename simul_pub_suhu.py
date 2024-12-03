#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:49:49 2024

@author: widhi
"""

import paho.mqtt.client as mqtt
import time

# Inisialisasi broker MQTT
broker = "localhost"  # Anda bisa menggunakan broker publik ini
port = 1883  # Port default untuk MQTT

# Inisialisasi topik dan pesan suhu
topic = "test/suhusrv6"
suhu = 10 # Suhu tetap 26'C

# Inisialisasi klien MQTT
client = mqtt.Client()

# Menghubungkan ke broker
client.connect(broker, port)

# Loop untuk mengirim pesan setiap detik
try:
    while True:
        # Mempublikasikan suhu ke topik
        message = f"Suhu: {suhu}°C"
        client.publish(topic, message)
        print(f"Published: {message}")
        
        # Tunggu 1 detik sebelum mengirim lagi
        time.sleep(1)
        suhu = suhu+2
except KeyboardInterrupt:
    print("Publisher dihentikan.")
    client.disconnect()
