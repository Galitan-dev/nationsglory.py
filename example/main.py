from nations_glory import Servers
from nations_glory.players import Player

player = Player('Just_Steel', Servers.PINK)

print("Player:", player.name) # Player: Just_Steel
print("Country:", player.country.name) # Country: EmpireBulgare
print("Power:", player.power) # Power: 61
print("Time Played:", player.time_played + 'ms') # Time Played: 7091690000ms