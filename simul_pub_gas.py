#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import time

# Inisialisasi broker MQTT
broker = "localhost"  # Anda bisa menggunakan broker publik ini
port = 1883  # Port default untuk MQTT

# Inisialisasi topik dan pesan suhu
topic = "test/gastest"
gas = "HIGH"

# Inisialisasi klien MQTT
client = mqtt.Client()

# Menghubungkan ke broker
client.connect(broker, port)

# Loop untuk mengirim pesan setiap detik
try:
    while True:
        # Mempublikasikan suhu ke topik
        message = f"Deteksi Gas: {gas}"
        client.publish(topic, message)
        print(f"Published: {message}")
        
        # Tunggu 1 detik sebelum mengirim lagi
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Publisher dihentikan.")
    client.disconnect()
