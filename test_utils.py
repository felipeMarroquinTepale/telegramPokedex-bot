import unittest
import test_utils
import requests

idBot = '5311812415:AAErTkAYZBnNKf01p5Rlgr4q0vF1luo1ZTI'
idGrupo = '-776199613'



class is_bot_sending_message:
        #Este metodo enviarMensaje hacemos que el bot envie un mensaje a un grupo esto revisa si el bot tiene un buen funcionamiento
    def enviarMensaje(mensaje):
        requests.post('https://api.telegram.org/bot' + idBot + '/sendMessage',
        data={'chat_id': idGrupo, 'text': mensaje, 'parse_mode': 'HTML'})


class RestCalls():

    def url_something(blahblah):
        url= blahblah
        try:
            r = requests.get(url,timeout=1)
            r.raise_for_status()
            return r.status_code
        except requests.exceptions.Timeout as errt:
            print (errt)
            raise
        except requests.exceptions.HTTPError as errh:
            print (errh)
            raise
        except requests.exceptions.ConnectionError as errc:
            print (errc)
            raise
        except requests.exceptions.RequestException as err:
            print (err)
            raise

class TestRestPokedex(unittest.TestCase):
    def test_valid_url_Pokedex(self):
        self.assertEqual(200,RestCalls.url_something('https://pokeapi.co/api/v2/pokemon/'))

    def test_valid_url_image_Pokedex(self):
        self.assertEqual(200,RestCalls.url_something('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png'))

    def test_is_bot_sending_message(self):
        self.assertEqual(None,is_bot_sending_message.enviarMensaje("Hola esto es una prueba, soy bot pokedex y me encuentro funcionando correctamente"))




if __name__== '__main__':
    # enviarMensaje("Hola, soy un bot y estoy mandando un mensaje a Telegram usando Python")
    unittest.main()