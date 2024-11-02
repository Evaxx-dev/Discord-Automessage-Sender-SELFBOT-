import requests
import time

token = "ur token" # change "ur token" with ur token
channel_id = 123456789 # change this with ur channel id
timeDelay = 15 # change this with the delay of ur msgs (prevents ratelimits)
message = "hi" # change this to the msg u want it to send

def sendMessage(token, channel_id, message):
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header)
    print(r.status_code)

while True:
    sendMessage(token, channel_id, message)
    time.sleep(timeDelay)
