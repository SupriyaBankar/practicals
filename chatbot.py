import nltk
from nltk.chat.util import Chat,reflections
import tkinter as tk
from tkinter import scrolledtext

pairs=[
    [r"hi|hello|hey",["hello,how can i assit you today?","hi there! hw can i help you"]],
    [r"how are you\?",["I m chatbot,but i am fine !how about you?","i am fine"]],
    [r"(.*)your name\?",["i am chatbot"]],
    [r"bye|goodbye",["goodbye!have a great day!"]]
]

chatbot=Chat(pairs,reflections)

def send_message():
    user_input = user_entry.get()
    if user_input.strip():     
        chat_history.insert(tk.END, f"You: {user_input}\n")
        response = chatbot.respond(user_input)
        chat_history.insert(tk.END, f"Chatbot: {response}\n\n")
        user_entry.delete(0, tk.END)
        
        # Auto-scroll to the bottom
        chat_history.yview(tk.END)
  
  
root = tk.Tk()
root.title("Simple Chatbot")
chat_history = scrolledtext.ScrolledText(root,wrap=tk.WORD,width=50,height=15)
chat_history.pack(padx=10,pady=10)

user_entry = tk.Entry(root,width=40)
user_entry.pack(padx=10,pady=10)
send_button = tk.Button(root,text="send",command=send_message)
send_button.pack(pady=5)

root.mainloop()
