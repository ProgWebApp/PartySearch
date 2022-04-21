# PartySearch : IGDB

![Icon](../icon.png)

## Table Of Contents

- [PartySearch : IGDB](#partysearch--igdb)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Getting Started](#getting-started)
    - [Requirements](#requirements)
    - [Environment Variables](#environment-variables)
    - [Build and Deploy](#build-and-deploy)
  - [Technologies Used](#technologies-used)

## Description

[IGDB](https://www.igdb.com/) is a global free online game database, it's API is completely free, so we can use it with a Python script to get fill our database with it.

## Getting Started

1) You need to install the [Requirements](#requirements)
2) Create the **igdb/.env** file with the **igdb/.env.sample** file by refering to the [Environment Variables](#environment-variables)
3) [Build and deploy](#build-and-deploy) the tool

### Requirements

- Docker
- Docker Compose

### Environment Variables

| Parameter | Value Example | Description |
|-|-|-|
| IGDB_GAME_NAME | Single Game "minecraft" or multiple game "minecraft dying-light" | Game to create or update in database |
| IGDB_CLIENT_ID | XXXXX | IGDB API Client ID |
| IGDB_CLIENT_SECRET | XXXXX | IGDB API Client Secret |
|  |  |  |

### Build and Deploy

```bash
cd igdb

# Build
docker-compose build

# Deploy
docker-compose up
```

You can also do it with a inline command (after build) :

```bash
cd igdb

# Single Game to update or create
docker-compose run --rm partysearch_igdb pdm run launch minecraft

# Multiple Game to update or create
docker-compose run --rm partysearch_igdb pdm run launch minecraft dying-light
```

## Technologies Used

- **Python 3**
- **PDM**
- **Python Libraries** :
  - [IGDB API Python](https://github.com/twitchtv/igdb-api-python)
  - [PyYAML](https://pypi.org/project/PyYAML/)
