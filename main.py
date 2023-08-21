import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "rinna/japanese-gpt2-medium"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

output = model.generate(max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
