import time
from mock_mqtt_client import MockMQTTClient  # Mock MQTT for testing locally
from smiley import handle_smiley_command, register_smiley_command  # Import functions
from react import handle_react_command, register_react_command  # Import functions
from ascii_art import handle_artascii_command, register_artascii_command  # Import functions

mqtt_client = MockMQTTClient("GHBot_Main_Client")

def main():
    mqtt_client.register_command("smiley", handle_smiley_command)
    mqtt_client.register_command("react", handle_react_command)
    mqtt_client.register_command("artascii", handle_artascii_command)
    
    print("GHBot command handlers registered and ready to receive commands.")

    while True:
        register_smiley_command(mqtt_client)
        register_react_command(mqtt_client)
        register_artascii_command(mqtt_client)
        time.sleep(5)  # Repeat every 5 seconds

if __name__ == "__main__":
    main()
