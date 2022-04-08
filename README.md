# PartySearch

[![License : MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Icon](./icon.png)

[Multiplayer icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/multiplayer)

## Table Of Contents

- [PartySearch](#partysearch)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Access](#access)
  - [Getting Started](#getting-started)
    - [Requirements](#requirements)
    - [Build](#build)
    - [Deploy](#deploy)
  - [Technologies Used](#technologies-used)
  - [Changelog](#changelog)
  - [Documentations](#documentations)
  - [Contributing](#contributing)
  - [Licence](#licence)

## Description

Static Website with coop and multi game referential.

You can add game to this static database with this [documentation](./docs/database.md).

## Access

- **Development (Local)** :
  - [PartySearch Development](http://localhost:8080)
- **Production (Local)** :
  - [PartySearch Production](http://localhost:8080)
- **Production** :
  - [PartySearch Production](https://partysearch)

## Getting Started

Here a sample of Docker Compose file : **docker-compose.yml**

```yaml
---
version: '3.6'

services:
  partysearch:
    container_name: 'partysearch'
    image: partysearch:1.0.0
    healthcheck:
      test: ["CMD", "wget", "-O", "/dev/null", "http://localhost:80"]
      interval: 1m
      timeout: 30s
      retries: 3
      start_period: 10s
    ports:
    - 8080:80
    restart: unless-stopped
```

### Requirements

- Docker
- Docker Compose

### Build

```bash
# Development
docker-compose -f docker-compose.dev.yml build

# Production
docker-compose build
```

### Deploy

```bash
# Development
docker-compose -f docker-compose.dev.yml up

# Production
docker-compose up
```

## Technologies Used

- **JS Framework** : [VueJS 3](https://vuejs.org/)
- **JS Libraries** :
  - [Axios](https://github.com/axios/axios)
  - [JS-YAML](https://github.com/nodeca/js-yaml)
  - [ListJS](https://listjs.com/)
  - [ChartJS](https://www.chartjs.org/)
- **CSS Framework** : [Materialize](https://materializecss.com/)

## Changelog

See [CHANGELOG](./CHANGELOG.md) for more information.

## Documentations

- [Ideas](./docs/ideas.md)
- [Commands](./docs/commands.md)
- [Database](./docs/database.md)
- [IGDB](./docs/igdb.md)

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## Licence

This project is licensed under the terms of the MIT license.

See [LICENSE](./LICENCE.md) for more information.
