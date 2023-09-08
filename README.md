# Listings

Search for any listed property, see available listings, all from the CLI

The purpose of this application is to provide an easier way for anyone hunting for any
type of real estate across the country to find it. It offers the ability for owners to list their
properties and users a way to filter through and query properties and property details.

### Features

- A user is able to list properties.
- A user will be able to filter through listings based on categories, location etc.
- A user can get the details for a specific property.
- A user can get owner or listing agent’s contact details for enquiry.
- An agent/owner can list a property.

## Setup Requirements

- Visual Studio Code, see [here](https://code.visualstudio.com/)
- Any [supported](https://www.python.org/downloads/) OS / environments / Windows Subsystem for Linux (WSL), details [here](https://learn.microsoft.com/en-us/windows/python/web-frameworks)
- Git and Github
- Python (Recommend version 3.10+), get the latest [here](https://www.python.org/downloads/)
- Pipenv, a Python virtualenv management tool, see details [here](https://pypi.org/project/pipenv/)
- SQLite

## Installation

- Clone/Download the code from the repository, navigate to the directory on the terminal
- Run `pipenv install` to install required packages
- Run `pipenv shell` to use the project in created project environment
- To run the program and access the features, run `cd lib`, in the lib directory, then run `python app.py` to start the app
- To populate the database, run `cd lib` if you're not in the `lib` directory, in the lib directory run `python seed.py` to generate sample data for the database

## Language(s)

- Python

## Packages

- SQLAlchemy
- Click
- Alembic
- Faker

## Author

[Eugene Aduogo](https://github.com/eugenemrg)

## License

Copyright (C) 2023

Licensed under GNUv3. See [license](/LICENSE)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.