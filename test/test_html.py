from re import I
from nations_glory.html import Dom
import pytest

def test_dom():
    pytest.dom = Dom.from_url('https://nationsglory.fr/profile/Just_Steel')

def test_player_name():
    assert type(pytest.dom) is Dom

    player_name = pytest.dom.find(
        tag='title'
    ).innerHTML.split(' ')[2]
    assert player_name == 'Just_Steel'

def test_player_country():
    assert type(pytest.dom) is Dom

    server_card = pytest.dom.find(
        tag='div', 
        classes=['card', 'server-tab'], 
        attributes={'data-server': 'pink'}
    )

    country_label = server_card.find(
        tag='h4',
        innerMatch=('^pays$', I)
    )

    country = country_label.parent.find(
        tag='a'
    ).innerHTML

    assert country == 'EmpireBulgare'