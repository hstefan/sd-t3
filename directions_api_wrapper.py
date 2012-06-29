import requests

class DirectionsError(Exception):
    pass

def get_directions_json(origin, dest, travel_mode='driving', sensor=False, language='pt-BR'):
    request_params = {
            'origin': origin,
            'mode': travel_mode,
            'sensor': 'true' if sensor else 'false',
            'language': language,
            'destination': ','.join(map(str, dest))
            }

    req = requests.get("http://maps.googleapis.com/maps/api/directions/json", params=request_params)

    if req.status_code == 200:
        return req.json
    elif req.status_code == 404:
        raise DirectionsError("Instruções não encontradas.")
    else:
        req.raise_for_status()
