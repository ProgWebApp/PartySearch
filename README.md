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

TODO Refactor Order + How to add games in database

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
TODO
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
  - TODO [muuri](https://muuri.dev/) OR [listjs](https://listjs.com/)
- **CSS Framework** : TODO [tailwindcss](https://tailwindcss.com/) OR [milligram](https://milligram.io/)

## Changelog

See [CHANGELOG](./CHANGELOG.md) for more information.

## Documentations

- [Ideas](./docs/ideas.md)
- [Commands](./docs/commands.md)

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## Licence

This project is licensed under the terms of the MIT license.

See [LICENSE](./LICENCE.md) for more information.
