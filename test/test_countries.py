from nations_glory import Servers
from nations_glory.countries import Country
from nations_glory.players import Player

def test_empire_bulgare_pink():
    country = Country('EmpireBulgare', Servers.PINK)

    assert country.leader == 'Firzonyx'
    assert country.claims == 521
    assert country.power == 1173

def test_thailande_blue():
    player = Player('Just_Steel', Servers.BLUE)
    country = player.country.fetch()

    assert country.leader == 'Just_Steel'
    assert country.claims == 317
    assert country.power == 618

def test_ecosse_lime():
    country = Country('Ecosse', Servers.LIME)

    assert country.leader== 'toto17du17'
    assert country.claims == 785
    assert country.power == 849