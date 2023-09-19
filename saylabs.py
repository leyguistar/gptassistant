#!/usr/bin/env python3
import requests
from playsound import playsound
import sys
import json
if(len(sys.argv) < 2):
    print(f'Usage: {sys.argv[0]} [text]')
    sys.exit(0)
with open('config.json','r') as h:
    keys = json.load(h)

CHUNK_SIZE = 1024
url = f"https://api.elevenlabs.io/v1/text-to-speech/{keys['eleven_labs_model']}"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": keys['eleven_labs_api_key']
}

data = {
  "text": sys.argv[1],
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.75
  }
}
try:
    response = requests.post(url, json=data, headers=headers)
    with open('/tmp/output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    playsound('/tmp/output.mp3')
except Exception as e:
    print(e)