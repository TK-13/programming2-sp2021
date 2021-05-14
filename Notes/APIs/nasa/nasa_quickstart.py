# https://api.nasa.gov/

import json
import requests

from PIL import Image
from io import BytesIO
from pprint import pprint


# NASA APOD (Astronomy Picture of the Day) API
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=4cNdVUuAaNk6hN7BNbX5wqDywLpxoVu6mtGjB8AB")
content = json.loads(response.content)
pprint(content)

url = content['url']
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()

# now set count to 2 and show all images


# now try to get an API key and use a different NASA API