from nations_glory import Servers
from nations_glory.countries import CountryRanks
from nations_glory.players import Player

def test_just_steel_pink():
    player = Player('Just_Steel', Servers.PINK)

    assert player.country.name == 'EmpireBulgare'
    assert player.country_rank == CountryRanks.OFFICIER
    assert player.power == 61

def test_just_steel_blue():
    player = Player('Just_Steel', Servers.BLUE)

    assert player.country.name == 'Thailande'
    assert player.country_rank == CountryRanks.LEADER
    assert player.power == 26

def test_fuzeiii_lime():
    player = Player('FuzeIII', Servers.LIME)

    
    assert player.country.name == 'EmpireBritannique'
    assert player.country_rank == CountryRanks.LEADER
    assert player.power == 56
    assert player.time_played == (
        12 * 24 * 3600 * 1000 +
        23 * 3600 * 1000 +
        22 * 60 * 1000 +
        10 * 1000
    )