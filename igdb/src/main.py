# Import standard libraries
from os import getenv
from urllib3 import PoolManager
from urllib.parse import urlencode
from json import loads
from sys import argv

# Import installed libraries
from igdb.wrapper import IGDBWrapper
from yaml import safe_load
from yaml import safe_dump


# Define variables
DATABASE_LOCATION = '/database/database.yml'
AUTH_URL = 'https://id.twitch.tv/oauth2/token'
FIELDS = """name, slug, summary, cover.url, genres.name"""


def getAccessToken(client_id, client_secret):
    request_data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
    }
    encoded_data = urlencode(request_data)
    http = PoolManager()
    response = http.request(
        'POST',
        f'https://id.twitch.tv/oauth2/token?{encoded_data}',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    data = loads(response.data.decode('utf-8'))
    if data.get('access_token') is None:
        raise Exception("Not Access Token !")
    return data.get('access_token')


def getGameData(game_name, client_id, access_token):
    wrapper = IGDBWrapper(client_id, access_token)
    data = wrapper.api_request(
        'games',
        f'fields {FIELDS}; limit 1; where slug="{game_name}";'
    )
    data = loads(data)
    if len(data) != 1:
        raise Exception("Game Data Request Error !")
    return data[0]


def isGameInDatabase(game_name, database):
    inDatabase = False
    for game in database:
        if game.get('slug') == game_name:
            inDatabase = True
    return inDatabase


def updateDatabase(game_data, database):
    data = {
        'name': game_data.get('name'),
        'slug': game_data.get('slug'),
        'summary': game_data.get('summary'),
        'icon': game_data.get('cover').get('url'),
        'genres': [genre.get('name') for genre in game_data.get('genres')],
        'coop': {
            'available': False,
            'min': 0,
            'max': 0
        },
        'multiplayer': {
            'available': False,
            'min': 0,
            'max': 0
        },
        'self_hosted': False,
        'download_size': 0.0,
        'installed_size': 0.0
    }
    database.append(data)
    return database


if __name__ == '__main__':
    GAME_NAME = getenv('IGDB_GAME_NAME').lower()
    if len(argv) > 1:
        GAME_NAME = argv[1].lower()
    CLIENT_ID = getenv('IGDB_CLIENT_ID')
    CLIENT_SECRET = getenv('IGDB_CLIENT_SECRET')

    database = None
    with open(DATABASE_LOCATION, "r") as database_file:
        database = safe_load(database_file)
        if database is None:
            database = []
    if (not isGameInDatabase(game_name=GAME_NAME, database=database)):
        access_token = getAccessToken(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        gameData = getGameData(game_name=GAME_NAME, client_id=CLIENT_ID, access_token=access_token)
        database = updateDatabase(game_data=gameData, database=database)
        with open(DATABASE_LOCATION, "w") as database_file:
            safe_dump(database, database_file)
        print('Add {} game to the database !'.format(gameData.get('name')))
    else:
        raise Exception("Game Already in Database !")
