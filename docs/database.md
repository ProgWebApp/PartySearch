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

This website contains a list of games with cooperation or multiplayer capacity. This game list is stored in a single file database in YAML Format to simplify the add of game.

Each game have several fields :

- **name** : Name of the Game
- **slug** : IGDB Name
- **summary** : Game Description
- **icon** : URL of icon of the game
- **genres** : List of genre of the game
- **coop** : Cooperation fields
  - **available** (true or false) : Cooperation available
  - **min** (2) : Minimum number of player
  - **max** (2) : Maximum number of player
- **multiplayer** : Multiplayer fields
  - **available** (true or false) : Multiplayer available
  - **min** (2) : Minimum number of player
  - **max** (2) : Maximum number of player
- **self_hosted** (true or false) : Server self hosted available
- **download_size** (in Gb) : Size of the game to download at start
- **installed_size** (in Gb) : Size of the game once it's installed

Exemple in YAML format :

```yaml
- name: ''
  slug: ''
  summary: ''
  icon : ''
  genres:
  - ''
  coop:
    available: true
    min: 2
    max: 4
  multiplayer:
    available: true
    min: 4
    max: 32
  self_hosted: true
  download_size: 1.5
  installed_size: 2
```

## How to add a new Game

To add a new game, you have two possibility :

### Fully Manual Mode

1) Go to [IGDB](https://www.igdb.com/) and search the game you want to add.
2) Check if the game not already exist in the database file (**src/database/database.yml**)
3) Get each information bellow and dispose these into the database file.

### Semi-Auto Mode

1) Go to [IGDB](https://www.igdb.com/) and search the game you want to add.
2) Get in the IGDB URL the "slug" name of the game (end of url, Dying Light = dying-light)
3) Fill the last data in the database file (coop, multiplayer, self_hosted, download_size and installed_size).
