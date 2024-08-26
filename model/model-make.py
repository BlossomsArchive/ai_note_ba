import MeCab
import gzip
import os

dir = "model/"
file_count = sum(os.path.isfile(os.path.join(dir,name)) for name in os.listdir(dir))

for i in range (1,file_count):
	input = open('model/base_{}.txt'.format(i), 'r', encoding='utf-8')

	mecab = MeCab.Tagger("-Owakati")

	output=""

	for line in input.read().split('\n'):
		splittedLine = ' '.join(mecab.parse(line).split())
		output += splittedLine
		output += '\n'

	input.close()

with gzip.open("/model.gz'", "wt", encoding="utf-8") as f:
	f.write(output)
