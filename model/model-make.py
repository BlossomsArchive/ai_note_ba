import MeCab

input = open('model/base.txt', 'r', encoding='utf-8') 
output = open('model.txt', 'w', encoding='utf-8') 

mecab = MeCab.Tagger("-Owakati")

for line in input.read().split('\n'):
	splittedLine = ' '.join(mecab.parse(line).split())
	output.write(splittedLine)
	output.write('\n')

input.close()
output.close()
