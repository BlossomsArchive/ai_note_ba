import MeCab
import os

dir = "model/"
file_count = sum(os.path.isfile(os.path.join(dir,name)) for name in os.listdir(dir))

for i in range (1,file_count):
	input = open('model/base_'+i+'.txt', 'r', encoding='utf-8') 
	output = open('model_'+i+'.txt', 'w', encoding='utf-8') 

	mecab = MeCab.Tagger("-Owakati")

	for line in input.read().split('\n'):
		splittedLine = ' '.join(mecab.parse(line).split())
		output.write(splittedLine)
		output.write('\n')

	input.close()
	output.close()
