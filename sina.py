import requests

app_key = "286067696"
app_sec = "8f62fea452cc5262217e6e27b1844699"
red_uri = "http://stamaimer.github.io"

# payload = {"client_id" : app_key, "redirect_uri" : red_uri}

payload = {"source" : app_key}

reply = requests.get("https://api.weibo.com/2/statuses/public_timeline.json", params = payload, verify = False)

print(reply.content)