import gradio as gr
# import calculator first then use the add inside the calculator
from mylib import calculator


def add_numbers(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return calculator.add(num1, num2)

with gr.Blocks() as demo:
    first_num = gr.Textbox(label="first num")
    second_num = gr.Textbox(label="second num")
    output = gr.Textbox(label="Result")
    add_butt = gr.Button("Add")
    add_butt.click(fn=add_numbers,inputs=[first_num,second_num], outputs=output)
    

demo.launch()
