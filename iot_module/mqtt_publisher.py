#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt #import library
import time

MQTT_BROKER = "localhost"
MQTT_TOPIC = "test_channel"

client = mqtt.Client("pyScript")
client.connect(MQTT_BROKER)
msg="Hello World!!"
client.publish(MQTT_TOPIC,msg)
print("Published {} over MQTT".format(msg))
counter=0
while counter<10:
    counter+=1
    client.publish(MQTT_TOPIC,"counter : {}".format(counter))
    print("Published counter : {}".format(counter))
    time.sleep(0.001)
client.disconnect()    