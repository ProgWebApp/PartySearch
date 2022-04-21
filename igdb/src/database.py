# Import installed libraries
from yaml import safe_load
from yaml import safe_dump


# Define variables
DATABASE_LOCATION = '/database'
MAIN_DATABASE_FILE = "_database.yml"


class MainDatabase():
    """
    Main Game Database Class
    """
    def __init__(self):
        self.games = []


    def add(self, id):
        if id not in self.games:
            self.games.append(id)


    def read(self):
        try:
            with open(f"{DATABASE_LOCATION}/{MAIN_DATABASE_FILE}", "r") as database_file:
                data = safe_load(database_file)
                if data is not None:
                    self.games = data
        except OSError:
            print("Main Database file doesn't exist !")


    def write(self):
        try:
            with open(f"{DATABASE_LOCATION}/{MAIN_DATABASE_FILE}", "w") as database_file:
                safe_dump(self.games, database_file)
        except OSError:
            print("Error when create the Main Database file !")


class GameDatabase():
    """
    Game Database Class
    """
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.url = ""
        self.summary = ""
        self.icon = ""
        self.genres = []
        self.size = 0.0
        self.coop = {
            'min': 0,
            'max': 0
        }
        self.multiplayer = {
            'min': 0,
            'max': 0
        }


    def update(self, game_data):
        self.id = game_data.get("id", self.id)
        self.name = game_data.get("name", self.name)
        self.url = game_data.get("url", self.url)
        self.summary = game_data.get("summary", self.summary)
        self.icon = game_data.get("icon", self.icon)
        self.genres = game_data.get("genres", self.genres)
        self.size = game_data.get("size", self.size)
        self.coop = game_data.get("coop", self.coop)
        self.multiplayer = game_data.get("multiplayer", self.multiplayer)


    def get_as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'summary': self.summary,
            'icon': self.icon,
            'genres': self.genres,
            'size': self.size,
            'coop': self.coop,
            'multiplayer': self.multiplayer
        }


    def read(self):
        try:
            with open(f"{DATABASE_LOCATION}/{self.id}.yml", "r") as database_file:
                data = safe_load(database_file)
                if data is not None:
                    self.name = data.get("name")
        except OSError:
            print("Game Database file doesn't exist !")


    def write(self):
        try:
            with open(f"{DATABASE_LOCATION}/{self.id}.yml", "w") as database_file:
                safe_dump(self.get_as_dict(), database_file)
        except OSError:
            print("Error when create the Game Database file !")
