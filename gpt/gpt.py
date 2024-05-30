import base64
import requests
from playsound import playsound
import Play_mp3


#import s
#os.environ[“OPENAI_API_KEY”] = “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”
# OpenAI API Key
#export HTTP_PROXY=http://127.0.0.1:10809
#from openai import OpenAI
#from config import OPENAI_API_KEY
api_key = "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"



# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/home/scott/下载/labixiaoxin.jpg"

# Getting the base64 string

'''
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())
print(response.json()['choices'][0]['message']['content'])

from synthesize_text import synthesize_text
synthesize_text(response.json()['choices'][0]['message']['content'])

from playsound import playsound
playsound('output.mp3')
'''

from openai import OpenAI
def chat(text):
  #from openai import OpenAI
  client = OpenAI(api_key=api_key)
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": text},
    ]
  )

  print(response.choices[0].message.content)
  #print(response['choices'][0]['message']['content'])
  from synthesize_text import synthesize_text
  synthesize_text(response.choices[0].message.content)

  Play_mp3.play('output.mp3')


def chat_image(image_path,text):
  base64_image = encode_image(image_path)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": text
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

  print(response.json())
  print(response.json()['choices'][0]['message']['content'])

  from synthesize_text import synthesize_text
  synthesize_text(response.json()['choices'][0]['message']['content'])

  Play_mp3.play('output.mp3')

#chat('hello,do you know who is uu?')
#chat_image(image_path,'what do you see?')