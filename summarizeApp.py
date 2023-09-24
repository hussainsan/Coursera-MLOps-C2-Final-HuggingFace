from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import gradio as gr

model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

def predict(prompt):
    # Count number of words in the input prompt 
    word_count_input = len(prompt.split())
    
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(input_ids, max_length=250, num_beams=4, early_stopping=True)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Count number of words in the summarized text
    word_count_summary = len(decoded.split())
    
    return decoded, f"Input Word Count: {word_count_input}", f"Summary Word Count: {word_count_summary}"

# Define the interface
iface = gr.Interface(
    fn=predict, 
    inputs=gr.components.Textbox(placeholder="Enter your text here..."),
    outputs=[
        gr.components.Textbox(label="Summarized Text"),
        gr.components.Textbox(label="Original Word Count"),
        gr.components.Textbox(label="Summarized Word Count")
    ]
)

iface.launch()
