# PartySearch : Database

![Icon](../icon.png)

## Table Of Contents

- [PartySearch : Database](#partysearch--database)
  - [Table Of Contents](#table-of-contents)
  - [Format](#format)
  - [How to add a new Game](#how-to-add-a-new-game)

## Format

This website contains a list of games with cooperation or multiplayer capacity. This game list is stored in a single file database in YAML Format to simplify the add of game.

Each game have several fields :

- **name** : Name of the Game
- **icon** : URL of icon of the game
- **banner** : URL of the banner of the game
- **release_date** (DD-MM-YYYY) : Date of release of the game
- **genres** : List of genre of the game
- **plateforms** : List of plateforms available
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
  icon : ''
  banner: ''
  release_date: ''
  genres:
  - ''
  plateforms:
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

TODO
