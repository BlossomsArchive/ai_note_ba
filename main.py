import markovify
import os
from misskey import Misskey
from atproto import Client, models
import time

input = open('./model.txt', 'r', encoding='utf-8')
model = markovify.NewlineText(input.read())
sentence = model.make_short_sentence(170, tries=10, max_overlap_ratio=0.7, max_overlap_total = 10)

note_text = sentence.replace(" ","")
print(note_text)

while True:
    try:
        #SNS投稿API
        # Misskey
        misskey_address = os.environ.get("MISSKEY_SERVER_ADDRESS")
        misskey_token = os.environ.get("MISSKEY_TOKEN")
        api = Misskey(misskey_address,misskey_token)
        input.close()
        api.notes_create(text=note_text,visibility='home')
    except:
        time.sleep(300)
    else:
        break
