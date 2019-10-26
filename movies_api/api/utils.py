from datetime import datetime

import requests
import urllib.parse


API_KEY = '338b2a2f'


def get_movie_data_from_title(title):
    """
    Get data from external source
    :param title:
    :return:
    """
    encoded_title = urllib.parse.quote_plus(title)
    api_route = f'http://www.omdbapi.com/?t={encoded_title}&apikey={API_KEY}'

    req = requests.get(api_route)

    status_code = req.status_code
    if status_code != 200:
        msg = {
            'error': 'Unable to connect to external source, check internet connection!'
        }
        return msg

    req_data = req.json()
    if req_data['Response'] == 'False':
        msg = {
            'error': req_data['Error']
        }
        return msg

    return req_data


def sanitize_external_movie_data(data):
    """
    Adapt data to database object
    Converts released to date object and runtime to int
    :return:
    """
    sanitized_data = {}
    for k, v in data.items():
        k = k.lower()
        sanitized_data[k] = v

    released = sanitized_data['released']
    if released != 'N/A':
        sanitized_data['released'] = datetime.strptime(released, '%d %b %Y').date()
    else:
        sanitized_data['released'] = None

    runtime = sanitized_data['runtime']
    if runtime != 'N/A':
        runtime = runtime.replace(' min', '')
        sanitized_data['runtime'] = int(runtime)
    else:
        sanitized_data['runtime'] = None

    poster = sanitized_data['poster']
    if poster == 'N/A':
        sanitized_data['poster'] = None

    return sanitized_data
