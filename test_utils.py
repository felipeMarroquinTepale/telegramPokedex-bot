import unittest
import test_utils
import requests

idBot = '5311812415:AAErTkAYZBnNKf01p5Rlgr4q0vF1luo1ZTI'
idGrupo = '-776199613'

# class TestUtilis(unittest.TestCase):


    #Este metodo enviarMensaje hacemos que el bot envie un mensaje a un grupo esto revisa si el bot tiene un buen funcionamiento
def enviarMensaje(mensaje):
    requests.post('https://api.telegram.org/bot' + idBot + '/sendMessage',
    data={'chat_id': idGrupo, 'text': mensaje, 'parse_mode': 'HTML'})



if __name__== '__main__':
    enviarMensaje("Hola, soy un bot y estoy mandando un mensaje a Telegram usando Python")
    # unittest.main()