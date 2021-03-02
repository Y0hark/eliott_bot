import logging
from utils import get_token
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters


updater = Updater(get_token('telegram'), use_context="True")
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#commands list
commands_list = []

#commands section
def help(update, context):
    update.message.reply_text("Bonjour! 👋\nJe suis Eliott 😁\nJe parle deux langues! Celle des commandes et celle des humains. Cela veut dire que tu peux me demander de faire quelque chose en tappant une commande de cette forme: /commande")
    update.message.reply_text("Mais tu peux aussi m'envoyer des messages tout ce qu'il y a de plus classique! Attention en revanche, ajouter des lettres ou autres caractères à ceux mentionnés en dessous ne fonctionnera pas.")
    update.message.reply_text("Toutes mes commandes : \n "+
    "/help - pour connaître l'étendue de mes pouvoirs 👍")
    update.message.reply_text("Les messages auquels je peux repondre :\n"+
    "bonjour")

commands_list.append(CommandHandler('help', help))

def greatings(update, context):
    if update.message.text.lower() == 'bonjour':
        update.message.reply_text("Bonjour! 👋 Que puis-je faire pour me rendre utile ?\nSi je peux me permettre un petit conseil, si jamais tu es perdu, essaies /help pour voir tout ce que je suis capable de faire! 😁")

commands_list.append(MessageHandler(Filters.text, greatings))



def main():
    
    
    
    
    #adding commands to the dispatcher
    for command in commands_list:
        dispatcher.add_handler(command)


    updater.start_polling()


    updater.idle()

if __name__ == '__main__':
    main()