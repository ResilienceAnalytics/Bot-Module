class MockMQTTClient:
    def __init__(self, client_id):
        self.client_id = client_id  # Unique client ID for tracking

    def publish(self, topic, message):
        # Print the simulated "publish" output to the console
        print(f"[PUBLISH] Topic: {topic} | Message: {message}")

    def connect(self, broker):
        # Simulate a connection to a broker
        print(f"[CONNECT] Connecting to broker at {broker} (Simulated)")
