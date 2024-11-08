# GHBot Modules

This repository provides custom modules for GHBot, implemented with Python, to expand GHBot’s capabilities on IRC. Each module listens for specific commands, sending back smileys, reactions, and ASCII art through an MQTT interface. This setup is tested with a mock MQTT client for easy local testing.

## Overview

GHBot Modules included in this repository:
- **Smiley Module** (`smiley.py`): Sends smiley faces in response to specific smiley-type commands.
- **React Module** (`react.py`): Sends reaction emojis based on predefined types.
- **ASCII Art Module** (`ascii_art.py`): Returns ASCII art for various themes like "hacker," "cat," and "bitcoin."

Each module uses a mock MQTT client (`mock_mqtt_client.py`) for testing. In a production environment, this can be replaced with a real MQTT client to interface with an actual MQTT broker.

## Modules & Commands

1. **Smiley Module (`smiley.py`)**  
   Responds to smiley-type commands with predefined smileys.
   - **Command**: `!smiley <type>`
   - **Types**: `:)`, `:(`, `;)`, `happy`, `sad`, `cool`

2. **React Module (`react.py`)**  
   Responds with reaction emojis based on the command type.
   - **Command**: `!react <type>`
   - **Types**: `clap`, `facepalm`, `laugh`, `shrug`, `cool`

3. **ASCII Art Module (`ascii_art.py`)**  
   Responds with ASCII art for a given theme.
   - **Command**: `!artascii <type>`
   - **Types**: `hacker`, `troll`, `alien`, `cat`, `bitcoin`

## Structure

- **`main.py`**  
  The main script initializes the modules and registers the commands with the MQTT broker.

- **`mock_mqtt_client.py`**  
  A mock MQTT client used for testing command handling and publishing locally.

- **`tests.py`**  
  Automated tests for all modules. Each command type is tested, ensuring the correct response or error message for invalid inputs.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ghbot-modules.git
   cd ghbot-modules
   ```

2. **Dependencies**  
   Ensure you have Python installed. The mock MQTT client used for testing does not require additional libraries.

3. **Run Tests**  
   To verify each module, run the test script:
   ```bash
   python tests.py
   ```
   This will output test results for each command and its response, simulating an actual interaction with GHBot.

## Example Usage

Commands can be sent via MQTT, and each module will respond as registered.

```plaintext
!smiley :)
Response: Smiley: (ᵔᴥᵔ)

!react laugh
Response: Reaction: (≧▽≦)

!artascii hacker
Response:
ASCII Art:
<ASCII Hacker Art>
```

## Customization

Each module is designed to be extensible:
- **Add New Smileys/Reactions/Art**: Add new types and corresponding characters in the `SMILEYS`, `REACTIONS`, or `ASCII_ARTS` dictionaries in their respective files.
- **Register New Commands**: Modify `main.py` to register additional commands or modules as needed.

## Test Results

The tests demonstrate the functionality and error handling for each module. Here’s a snippet from the test results:

```plaintext
Running Smiley Command Tests for all types:
[PUBLISH] Topic: GHBot/to/bot/register | Message: cmd=!smiley|descr=Send a random smiley based on type|agrp=everyone|athr=YourName|loc=smiley_module
- Testing with valid smiley type ':)'
[PUBLISH] Topic: GHBot/to/irc/channel/privmsg | Message: Smiley: :)
...
Running ASCII Art Command Tests for all types:
[PUBLISH] Topic: GHBot/to/bot/register | Message: cmd=!artascii|descr=Send ASCII art based on type|agrp=everyone|athr=YourName|loc=ascii_art_module
- Testing with valid ASCII art type 'hacker'
[PUBLISH] Topic: GHBot/to/irc/channel/privmsg | Message: ASCII Art:
<ASCII Hacker Art>
```

## License

This project is licensed under the MIT License.

---

