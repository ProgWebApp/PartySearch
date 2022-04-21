# Import standard libraries
from urllib3 import PoolManager
from urllib.parse import urlencode
from json import loads

# Import installed libraries
from igdb.wrapper import IGDBWrapper


# Define variables
AUTH_URL = 'https://id.twitch.tv/oauth2/token'
FIELDS = """name, slug, url, summary, cover.url, genres.name,
multiplayer_modes.campaigncoop, multiplayer_modes.lancoop,
multiplayer_modes.offlinecoop, multiplayer_modes.offlinecoopmax,
multiplayer_modes.offlinemax, multiplayer_modes.onlinecoop,
multiplayer_modes.onlinecoopmax, multiplayer_modes.onlinemax"""


def getAccessToken(client_id, client_secret):
    """
    Get Access Token from IGDB.
    """
    # Prepare Credentials
    request_data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
    }
    encoded_data = urlencode(request_data)

    # Request the Access Token
    http = PoolManager()
    response = http.request(
        'POST',
        f'{AUTH_URL}?{encoded_data}',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    # Get the Access Token
    data = loads(response.data.decode('utf-8'))
    if data.get('access_token') is None:
        raise Exception("Not Access Token !")
    return data.get('access_token')


def getGameData(game_name, client_id, access_token):
    """
    Get Game Data from IGDB.
    """
    wrapper = IGDBWrapper(client_id, access_token)
    data = wrapper.api_request(
        'games',
        f'fields {FIELDS}; limit 1; where slug="{game_name}";'
    )
    data = loads(data)
    if len(data) != 1:
        raise Exception("Game Data Request Error !")
    return data[0]


def getFormattedGameData(game_data):
    """
    Format Game Data for the Database
    """
    data = {
        'id': game_data.get('slug'),
        'name': game_data.get('name'),
        'url': game_data.get('url'),
        'summary': game_data.get('summary'),
        'icon': game_data.get('cover').get('url'),
        'genres': [genre.get('name') for genre in game_data.get('genres')],
        'size': 0.0
    }
    if game_data.get('multiplayer_modes'):
        for mode in game_data.get('multiplayer_modes'):
            if mode.get('campaigncoop') or mode.get('lancoop') or mode.get('offlinecoop') or mode.get('onlinecoop'):
                min_coop = 0
                max_coop = max((mode.get('offlinecoopmax', 0), mode.get('onlinecoopmax', 0)))
                if max_coop > 0:
                    min_coop = 2
                data['coop'] = {
                    'min': min_coop,
                    'max': max_coop
                }
            min_multi = 0
            max_multi = max((mode.get('offlinemax', 0), mode.get('onlinemax', 0)))
            if max_multi > 0:
                min_multi = 2
            data['multiplayer'] = {
                'min': min_multi,
                'max': max_multi
            }
    else:
        data['coop'] = {'min': 0, 'max': 0}
        data['multiplayer'] = {'min': 0, 'max': 0}
    return data
