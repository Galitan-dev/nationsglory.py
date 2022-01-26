
# NationsGlory.py [![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/galitan-dev/nationsglory.py/blob/main/LICENSE)

A python library that retrieves information from nationsglory.fr, just for you!


## Authors

- [@galitan-dev](https://www.github.com/galitan-dev)


## Features

- GET player informations
- GET country informations


## Installation

Install nations-glory with pip

```bash
pip install nations-glory
```
    
## Usage/Examples

```python
from nations_glory import Servers
from nations_glory.players import Player
from nations_glory.countries import Country

player = Player('Just_Steel', Servers.PINK)

print("\nPlayer:", player.name)
print("Country:", player.country.name)
print("Power:", player.power)
print("Time Played:", str(player.time_played) + 'ms')

country = Country('EmpireBulgare', Servers.PINK)
# country = player.country.fetch()

print("\nCountry:", country.name)
print("Leader:", country.leader) 
print("Claims", country.claims)
print("Power:", player.power)

# OUTPUT:
#
# Player: Just_Steel
# Country: EmpireBulgare
# Power: 61
# Time Played: 7334691000ms
#
# Country: EmpireBulgare
# Leader: Firzonyx
# Claims 521
# Power: 61
```


## Dependencies

[![python3.9.0](https://img.shields.io/badge/python-3.9.0-brightgreen?style=for-the-badge&logo=python&logoColor=brightgreen)](https://www.python.org/downloads/release/python-390/)
[![requests==2.22.0](https://img.shields.io/badge/requests-2.22.0-blue?style=for-the-badge)](https://pypi.org/project/requests/2.22.0/)
[![html-to-json==1.0.1](https://img.shields.io/badge/html--to--json-1.0.1-blue?style=for-the-badge)](https://pypi.org/project/json-to-html/1.0.1/)


## License

[MIT](https://choosealicense.com/licenses/mit/)
