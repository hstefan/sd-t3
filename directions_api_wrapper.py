from util import response_to_json
from urllib.parse import urlencode

class DirectionsError(Exception):
    pass
    
def get_directions(origin, dest, travel_mode='driving', sensor=False):
    directions_api_url = "http://maps.googleapis.com/maps/api/directions/json?"
    language = 'pt-BR'
    
    request_url = directions_api_url + urlencode({'origin' : origin, 
        'destination' : dest, 'mode' : travel_mode, 'sensor' : 'true' if sensor == True else 'false'})
    try:
        dir = response_to_json(request_url)
        return dir
    except HTTPError as e:
        if e.code == 404:
            raise DirectionsError('Direcoes nao encontradas.') from e
        else:
            raise