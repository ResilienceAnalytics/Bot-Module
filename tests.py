from mock_mqtt_client import MockMQTTClient  # Mock client for testing
from smiley import handle_smiley_command, register_smiley_command
from react import handle_react_command, register_react_command
from ascii_art import handle_artascii_command, register_artascii_command

print("Starting GHBot Local Command Tests...\n")

client = MockMQTTClient("GHBot_Test_Client")

smiley_types = [":)", ":(", ";)", "happy", "sad", "cool"]
reaction_types = ["clap", "facepalm", "laugh", "shrug", "cool"]
ascii_art_types = ["hacker", "troll", "alien", "cat", "bitcoin"]

def test_all_smiley():
    print("Running Smiley Command Tests for all types:")
    register_smiley_command(client)
    for smiley_type in smiley_types:
        print(f"- Testing with valid smiley type '{smiley_type}'")
        handle_smiley_command(smiley_type, client)
    print("- Testing with invalid smiley type 'unknown'")
    handle_smiley_command("unknown", client)
    print("\n")

def test_all_react():
    print("Running Reaction Command Tests for all types:")
    register_react_command(client)
    for reaction_type in reaction_types:
        print(f"- Testing with valid reaction type '{reaction_type}'")
        handle_react_command(reaction_type, client)
    print("- Testing with invalid reaction type 'unknown'")
    handle_react_command("unknown", client)
    print("\n")

def test_all_ascii_art():
    print("Running ASCII Art Command Tests for all types:")
    register_artascii_command(client)
    for art_type in ascii_art_types:
        print(f"- Testing with valid ASCII art type '{art_type}'")
        handle_artascii_command(art_type, client)
    print("- Testing with invalid ASCII art type 'unknown'")
    handle_artascii_command("unknown", client)
    print("\n")

test_all_smiley()
test_all_react()
test_all_ascii_art()

print("All tests completed.\n")
