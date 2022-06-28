import json
import requests




def pokedex(id_name):
    #print('Este metodo sera para consumir la api de pokedex y seleccionar algunas caracteristicas de los pokemones mediante un ID')
    try:
        output= ""
        url = "https://pokeapi.co/api/v2/pokemon/{}/"
        #get request for API information retrieval
        final_url = url.format(id_name)
        response = requests.get(final_url)
        response = response.content
        #json to python dictionary convertion
        information=json.loads(response)
        # print(information)
        #getting all the information
        output += f"<b>ID:</b> {str(information['id'])} \n"
        output += f"<b>Name:</b> {str(information['name'])}\n"
        output += f"<b>Height:</b> {str(information['height'])}\n"
        output += f"<b>Weight:</b> {str(information['weight'])}\n"
        all_types=information['types']
        types = ""
        for type_ in all_types:
            types += f"{type_['type']['name']} "


        output += f"<b>Types:</b> {str(types)} \n"
        all_moves=information['moves']


        moves = ""
        #getting 5 moves of the pokemon
        if len(all_moves) < 6:
            for i in range(len(all_moves)):
                moves += f"<b>{i+1}:</b> {all_moves[i]['move']['name']} \n"
        else:
            for i in range(6):
                moves += f"<b>{i+1}:</b> {all_moves[i]['move']['name']} \n"
        output += f"<b>Moves:\n</b> {moves} \n"

        print(output)

        if information['id'] <= 890:
            photo_url = f"https://pokeres.bastionbot.org/images/pokemon/{information['id']}.png"
            # photo_url = f"https://unpkg.com/pokeapi-sprites@2.0.2/sprites/pokemon/other/dream-world/{information['id']}.svg"
            # photo_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{information['id']}.png "
        else:
            photo_url = None



    except json.decoder.JSONDecodeError:
        output = None
        photo_url = None
    return output,photo_url





