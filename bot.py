from asyncore import dispatcher
from telegram.ext import *
import config_file
from pokedex import pokedex
import json

#Comando de inicio o start, cuando el usuario digite /start el  bot tomara esta funcions
def start_command(update,context):
    #Obtenemos el nombre del usuario
    username = update.message.chat.first_name
    update.message.reply_text(f"¡Hey, ¿como estas? {username}. Dejame darte la bienvenida al mundo de los pokemones :)")
    update.message.reply_text("Por favor ingrese un nombre valido de un pokemon o dame un ID del 1-890 para darte informacion de tu pokemon")

#Cuando el usuario digite /help el bot tomara esta funcion para poder ayudar al usuario
def help_command(update,context):
    username = update.message.chat.first_name
    update.message.reply_text(f'Oh veo que quieres ayuda para iniciar, mira {username} solo tienes que ingresar un ID o nombre de un pokemon valido (el ID esta entre 1-890)')

#Cuando nuestro bot enfrente algun error durante la ejecucion tomara esta funcion para poder manejarlo
def error(update,context):
    #El error que arroje solo lo imprimiremos en la consola
    print(f"{update} error causado por --->  {context.error}")
    #El bot dira
    print("\nPa que te informes de lo que paso joven")


#Cuando el usuario envie un ID o un name de un pokemon se vendra aca para poder responder
def message_response(update,context):
    #Recuperamos lo que el usuario texteo
    text = str(update. message.text).lower()
    #Recuperamos el nombre del usuario
    username = update.message.chat.first_name


    if text in ("hola pokedex","pokedex","Pokedex","quiero saber de un pokemon"):
        response = (f"<b>¡Hey ¿como estas? ! {username}, ingresa un nombre valido de un pokemon o dame un ID del 1-890 para darte informacion de tu pokemon </b>")
    else:
        #Vamos a extraer con el ID o name los datos de la api pokedex que se encuentra en el pokedex.py
        response,photo_url = pokedex(text)
        if response != None and photo_url != None:
            chat_id = update.message.chat_id
            context.bot.send_photo(chat_id=chat_id,photo=photo_url)
        else:
            response = "Lo siento amigo no te entiendo. Por favor ingrese un ID o nombre valido de un pokemon para poder obtener informacion "

    update.message.reply_text(response,parse_mode='HTML')



def main():
    #Comenzamos a consumir el bot que creamos en bot father en telegram
    #El actualizador se inicializa proporcionando la api_key que almacenamor en config_file.py
    updater = Updater(config_file.api_key, use_context = True)
    #El despachador se inicializa
    dp = updater.dispatcher
    #Agregamos los dos controladores de comandos que se usaran para manejar el comando /start o /help en Telegram
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    #El controlador de mensajes también se agrega para manejar cualquier mensaje enviado por el usuario
    dp. add_handler(MessageHandler(Filters.text,message_response))
    #El controlador de errores se agrega, para manejar cualquier error que se presente
    dp.add_error_handler(error)
    #El actualizador se actualiza cada 3 segundos
    updater.start_polling(3)
    updater.idle()

print("Bot started running")


if __name__ == "__main__":
    main()
