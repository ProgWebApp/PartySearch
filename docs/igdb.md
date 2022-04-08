# PartySearch : IGDB

![Icon](../icon.png)

## Table Of Contents

- [PartySearch : IGDB](#partysearch--igdb)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Getting Started](#getting-started)
    - [Requirements](#requirements)
    - [Build and Deploy](#build-and-deploy)
  - [Technologies Used](#technologies-used)

## Description

[IGDB](https://www.igdb.com/) is a global free online game database, it's API is completely free, so we can use it with a Python script to get fill our database with it.

## Getting Started

1) Copy the **igdb/.env.sample** file into **igdb/.env** file and complete it with your credentials
2) [Build and deploy](#build-and-deploy) the tool

### Requirements

- Docker
- Docker Compose

### Build and Deploy

```bash
# Build
docker-compose build

# Deploy
docker-compose up
```

You can also do it with a inline command (after build) :

```bash
docker-compose run --rm partysearch_igdb pdm run launch minecraft
```

## Technologies Used

- **Python 3**
- **PDM**
- **Python Libraries** :
  - [IGDB API Python](https://github.com/twitchtv/igdb-api-python)
  - [PyYAML](https://pypi.org/project/PyYAML/)
