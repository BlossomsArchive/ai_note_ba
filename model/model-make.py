import MeCab
import gzip
import os

dir = "model/"
file_count = sum(os.path.isfile(os.path.join(dir, name)) for name in os.listdir(dir))

output = ""

for i in range(1, file_count + 1):  # 最後のファイルも含めるように修正
    file_path = os.path.join(dir, 'base_{}.txt'.format(i))

    with open(file_path, 'r', encoding='utf-8') as file:
        mecab = MeCab.Tagger("-Owakati")
        for line in file:
            splittedLine = ' '.join(mecab.parse(line).split())
            output += splittedLine
            output += '\n'

with gzip.open("model.gz", "wt", encoding="utf-8") as f:  # ファイルパスを修正
    f.write(output)
