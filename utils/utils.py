import json

def get_token(token_service_name):
    f = open('../data/token.json')
    data = json.load(f)
    
    if token_service_name == "telegram":
        token = data['token'][0]['value']
    
    elif token_service_name == "navitia":
        token = token = data['token'][1]['value']       
    
    return token

