from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chat = ChatBot("Basico")
talk =["hola","¿que tal","tengo una pregunta",
"Si, dime","¿La comida en mexico es buena?","SI,es deliciosa"]

trainer = ListTrainer(chat)
trainer.train(talk)
while True:
    #"me salgo con control c"
    peticion = input("Tu: ")
    respuesta= chat.get_response(peticion)
    print("bot: ",respuesta)
