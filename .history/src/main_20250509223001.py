import gradio as gr
import random

class ChatApp:
    def __init__(self):
        self.greetings = ["こんにちは！", "元気ですか？", "お話しましょう！"]
        self.acknowledgements = ["なるほど。", "そうですね。", "わかります。", "たしかに。", "はいはい。"]

    def respond(self, message, chat_history):
        bot_message = random.choice(self.acknowledgements)
        chat_history.append((message, bot_message))
        return bot_message, chat_history

    def create_ui(self):
        with gr.Blocks() as demo:
            chatbot = gr.Chatbot()
            msg = gr.Textbox()
            clear = gr.Button("Clear")

            msg.submit(self.respond, [msg, chatbot], [msg, chatbot])
            clear.click(lambda: None, None, chatbot, queue=False)

        return demo

if __name__ == "__main__":
    chat_app = ChatApp()
    demo = chat_app.create_ui()
    demo.launch()
