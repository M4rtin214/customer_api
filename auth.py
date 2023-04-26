from flask import request



API_KEY = "b3cda5ca-c1fb-17e9-883a-8086f2a23d15"

def api_key_required(decorated_method):
    def wrapper(*args, **kwargs):
        for i in request.headers:
            if i[0] == 'Api-Key' and i[1] == API_KEY:
                return decorated_method(*args, **kwargs)
        else:
            return {'error':'valid API key missing!'}, 401
    return wrapper