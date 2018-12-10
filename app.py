"""Simple Slack API testing"""
import os
from slackclient import SlackClient

# get from environment variable
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
SLACK_CLIENT = SlackClient(SLACK_TOKEN)


def get_channel_lisitng():
    """ should return two keys: ok and channels
        ok should return True if API call was successful
        channels will then return a list of channels
    """
    channels_call = SLACK_CLIENT.api_call("channels.list")
    if channels_call.get("ok"):
        return channels_call["channels"]
    return None


if __name__ == "__main__":
    channels = get_channel_lisitng()
    if channels:
        print("Channels: ")
        for c in channels:
            print(c["name"] + " (" + c["id"] + ")")
    else:
        print("Unable to authenticate.")
