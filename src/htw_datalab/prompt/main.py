import ollama
from ollama import chat

if __name__=="__main__":
    print('hola')
    conversation = [
    {"role": "user", "content": "how old is the earth?"}
    ]
    #reply = chat(model='llama3.3', messages=conversation)
    #print(reply.message.content)
    print(ollama.list())
    print(ollama.show('llama3.3'))