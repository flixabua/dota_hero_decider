# This code is currently not functional and is a work in progress.
# It is intended to be used with the Steam and Dota2 Python libraries.  
# Let's see where it goes.
from steam.client import SteamClient
from dota2.client import Dota2Client

def load_api_key(filepath=".steam_api_key"):
    """Load the Steam API key from a file."""
    with open(filepath, "r") as f:
        return f.read().strip()

if __name__ == "__main__":
    client = SteamClient()
    client.login("flixabua", login_key=load_api_key())
    print("Steam client initialized.")
    dota = Dota2Client(client)
    client.run_forever()