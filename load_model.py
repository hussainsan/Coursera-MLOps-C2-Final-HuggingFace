"""Loading a model from a file."""

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


# model = AutoModelForSeq2SeqLM.from_pretrained("summarizeApp")
# tokenizer = AutoTokenizer.from_pretrained("summarizeApp")

model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

# #open the file with utf-8 encoding
with open("text.txt", encoding="utf-8") as f:
    text = f.read()

word_count = len(text.split())
print(word_count)
input_ids = tokenizer.encode(text, return_tensors="pt")
outputs = model.generate(input_ids, max_length=250, num_beams=4, early_stopping=True)
decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(decoded)