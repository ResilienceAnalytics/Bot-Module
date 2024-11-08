import random
from mock_mqtt_client import MockMQTTClient

REACTIONS = {
    "clap": ["(clap)", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "٩(◕‿◕｡)۶"],
    "facepalm": ["(－‸ლ)", "(－_－)", "(>ლ)", "(；一_一)"],
    "laugh": ["(≧▽≦)", "(＾▽＾)", "(*≧ω≦)", "(*≧▽≦)ﾉｼ"],
    "shrug": ["¯\\_(ツ)_/¯", "╮(︶▽︶)╭"],
    "cool": ["(⌐■_■)", "(•_•)⌐■-■", "(￣ー￣)b"]
}

def handle_react_command(reaction_type, client):
    if reaction_type in REACTIONS:
        reaction = random.choice(REACTIONS[reaction_type])
        client.publish("GHBot/to/irc/channel/privmsg", f"Reaction: {reaction}")
    else:
        client.publish("GHBot/to/irc/channel/privmsg", "Unknown reaction type.")

def register_react_command(client):
    client.publish("GHBot/to/bot/register", "cmd=!react|descr=Send a reaction emoji based on type|agrp=everyone|athr=YourName|loc=react_module")
