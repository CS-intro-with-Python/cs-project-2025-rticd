import requests
import sys

response = requests.get("http://localhost:5000")
if(response.status_code != 200):
    sys.exit(1)

