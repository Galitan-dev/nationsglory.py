from nations_glory import Servers
from nations_glory.players import Player, PlayerCard

def test_just_steel_pink():
    player = Player('Just_Steel', Servers.PINK)

    assert player.country == 'EmpireBulgare'
    assert player.country_rank == 'Officier'
    assert player.power == 61

def test_just_steel_blue():
    player = Player('Just_Steel', Servers.BLUE)

    assert player.country == 'Thailande'
    assert player.country_rank == 'Leader'
    assert player.power == 26

def test_fuzeiii_orange():
    player = Player('FuzeIII', Servers.LIME)

    assert player.country == 'EmpireBritannique'
    assert player.country_rank == 'Leader'
    assert player.power == 56