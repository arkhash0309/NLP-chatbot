from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Alpha")
trainer = ListTrainer(chatbot)

trainer.train(['Hi','Hello','How are you?','I am fine and you?','Great','What are you Doing?','nothing just roaming around.'])

while True:
    input_data = input("You: ")
    response = chatbot.get_response(input_data)
    print("Alpha: ",response)