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