import subprocess
import time

# Run MQTT Subscriber
sub_process = subprocess.Popen(["python", "mqtt_subscriber.py"])
print("MQTT Subscriber is running...")

# Wait for the subscriber to connect before starting the publisher
time.sleep(2)

# Run MQTT Publisher
pub_process = subprocess.Popen(["python", "mqtt_publisher.py"])
print("MQTT Publisher is running...")

