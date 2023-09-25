import markovify
import os
from misskey import Misskey
import time

input = open('./model.txt', 'r', encoding='utf-8')
model = markovify.NewlineText(input.read())
sentence = model.make_sentence()

note_text = sentence.replace(" ","")
print(note_text)

#SNS投稿API
# Misskey
misskey_address = os.environ.get("MISSKEY_SERVER_ADDRESS")
misskey_token = os.environ.get("MISSKEY_TOKEN")
api = Misskey(misskey_address)
api.token = misskey_token
input.close()

while True:
    try:
        api.notes_create(text=note_text)
    except:
        time.sleep(300)
    else:
        break