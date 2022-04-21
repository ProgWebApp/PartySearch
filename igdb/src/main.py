# Import standard libraries
from os import getenv
from sys import argv
from unicodedata import name

# Import created libraries
from utils import getAccessToken
from utils import getGameData
from utils import getFormattedGameData
from database import MainDatabase
from database import GameDatabase


# Define variables
CLIENT_ID = getenv('IGDB_CLIENT_ID')
CLIENT_SECRET = getenv('IGDB_CLIENT_SECRET')
GAME_LIST = getenv('IGDB_GAME_NAME').split(' ')
if len(argv) > 1:
    GAME_LIST = argv[1:]


# Main Program
if __name__ == '__main__':
    print("Get Access Token ...")
    access_token = getAccessToken(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    print("Access Token Get !\n")

    # Main Database
    print("Init or Import Main Database ...")
    main_database = MainDatabase()
    main_database.read()
    print("Main Database Ready !\n")

    games = []

    print("Register Games ...\n")
    for game in GAME_LIST:
        # Create Game Database
        print(f"Init or Import Game Database for game : {game} ...")
        game_database = GameDatabase(id=game)
        game_database.read()
        print(f"Game Database for game : {game} Ready !")

        # Get Game Data for this Game
        print(f"Get Data for game : {game} ...")
        game_data_raw = getGameData(
            game_name=game,
            client_id=CLIENT_ID,
            access_token=access_token
        )
        game_data = getFormattedGameData(game_data=game_data_raw)
        print(f"Data Get for game : {game} !")

        # Update Databases
        print(f"Update Game Database for game : {game} ...")
        game_database.update(game_data=game_data)
        main_database.add(id=game_database.id)
        games.append(game_database)
        print(f"Game Database for game : {game} Updated !\n")

    # Write and Save Main Database
    print("Write and save the Main Database file ...")
    main_database.write()
    print("Save of the Main Database file Complete !\n")

    print("Write and save each Game Database file ...\n")
    for game in games:
        print(f"Write and save the Game Database file for game : {game.name} ...")
        game.write()
        print(f"Save of the Game Database file for game : {game.name} Complete !\n")

    print("Sequence Complete !")
    exit(0)
