import sys
import requests

# for element in sys.path:
	
# 	print element

response = requests.get("http://www.walmart.com/")

print response.content

https://api.weibo.com/oauth2/authorize#