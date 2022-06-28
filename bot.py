import imp
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