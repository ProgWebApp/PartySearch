# PartySearch : Database

![Icon](../icon.png)

## Table Of Contents

- [PartySearch : Database](#partysearch--database)
  - [Table Of Contents](#table-of-contents)
  - [Format](#format)
  - [How to add a new Game](#how-to-add-a-new-game)
    - [Fully Manual Mode](#fully-manual-mode)
    - [Semi-Auto Mode](#semi-auto-mode)

## Format

This website contains a list of games with cooperation or multiplayer capacity. This game list is stored in a multi file database in YAML Format to simplify the add of game.

Each game have several fields :

- **name** : Name of the Game
- **id** : IGDB Name or Game ID (Name in lowercase without space)
- **url** : URL of Game informations (IGDB URL or Game Official Page)
- **summary** : Game Description
- **icon** : URL of icon of the game
- **genres** : List of genre of the game
- **coop** : Cooperation fields
  - **min** : Minimum number of player (minimum of 2)
  - **max** : Maximum number of player (minimum of 2 and -1 for infinite)
- **multiplayer** : Multiplayer fields
  - **min** : Minimum number of player (minimum of 2)
  - **max** : Maximum number of player (minimum of 2 and -1 for infinite)
- **size** (in Gb) : Size of the game

Exemple in YAML format :

```yaml
name: "Dying Light"
id: "dying-light"
url: "https://www.igdb.com/games/dying-light"
summary: "Zombie Game."
icon : "//images.igdb.com/igdb/image/upload/t_thumb/co3wml.jpg"
genres:
- "Shooter"
- "Role-playing (RPG)"
- "Adventure"
coop:
  min: 2
  max: 4
multiplayer:
  min: 0
  max: 0
size: 40.0
```

## How to add a new Game

To add a new game, you have two possibility :

### Fully Manual Mode

1) Go to [IGDB](https://www.igdb.com/) and search the game you want to add or search on the **official game website**.
2) Check if the game not already exist in the **database main file** (**src/database/_database.yml**) (use CTRL + F to find the game name in lowercase without space)
   1) If the game **already exist**, you can **update** it with the edit of the file listed in the **database main file** (**src/database/_database.yml**)
   2) Else get each information bellow and dispose these into a **new database file** with the **id of the game** as **file name** and register it in the **database main file** (**src/database/_database.yml**).

### Semi-Auto Mode

1) Go to [IGDB](https://www.igdb.com/) and search the game you want to add.
2) Get in the IGDB URL the "slug" or "id" name of the game (end of url, game name in lowercase without space, Dying Light = dying-light)
3) Use the [IGDB Script](./igdb.md) to **update** or **create** a **new entry** for this game in the **database**.
4) Fill the **last data** in the database file (coop, multiplayer, and size) **if needed**.

Great and thanks for update our database.
