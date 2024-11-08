import random
from mock_mqtt_client import MockMQTTClient

SMILEYS = {
    ":)": [":)", "(^‿^)", "(•‿•)", "(ᵔᴥᵔ)"],
    ":(": ["(╥﹏╥)", "(︶︹︺)", "(｡╯︵╰｡)", "(ಥ﹏ಥ)"],
    ";)": [";)", "(^_~)", "(¬‿¬)", "(⊙‿⊙)"],
    "happy": ["(^‿^)", "(＾◡＾)", "(•‿•)", "(ᵔᴥᵔ)"],
    "sad": ["(╥﹏╥)", "(︶︹︺)", "(｡╯︵╰｡)", "(ಥ﹏ಥ)"],
    "cool": ["(⌐■_■)", "(▀̿Ĺ̯▀̿ ̿)", "(￣ー￣)b"]
}

def handle_smiley_command(smiley_type, client):
    if smiley_type in SMILEYS:
        smiley = random.choice(SMILEYS[smiley_type])
        client.publish("GHBot/to/irc/channel/privmsg", f"Smiley: {smiley}")
    else:
        client.publish("GHBot/to/irc/channel/privmsg", "Unknown smiley type.")

def register_smiley_command(client):
    client.publish("GHBot/to/bot/register", "cmd=!smiley|descr=Send a random smiley based on type|agrp=everyone|athr=YourName|loc=smiley_module")
