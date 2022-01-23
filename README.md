
# NationsGlory.py

A python library that collects information from nationsglory.fr, just for you.


## Authors

- [@galitan-dev](https://www.github.com/galitan-dev)


## Features

- GET player informations
- GET country informations


## Installation

Install ng with pip

```bash
pip install ng
```
    
## Usage/Examples

```python
from nations_glory import Servers
from nations_glory.players import Player

player = Player('Just_Steel', Servers.PINK)

print("Player:", player.name) # Player: Just_Steel
print("Country:", player.country) # Country: EmpireBulgare
print("Power:", player.power) # Power: 61
print("Time Played:", player.time_played) # Time Played: 2 mois 28 j 12 h 51 m 54 s 
```


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/galitan-dev/nationsglory.py/blob/master/LICENSEs)
