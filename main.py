import markovify

input = open('./model.txt', 'r', encoding='utf-8')
model = markovify.NewlineText(input.read())
sentence = model.make_sentence()

note_text = sentence.replace(" ","")
print(note_text)

input.close()