import requests
import json
from pprint import pprint

# get random affirmations :)
for i in range(10):
    affirmation = json.loads(requests.get("https://www.affirmations.dev").text)
    pprint(affirmation.get('affirmation'))
