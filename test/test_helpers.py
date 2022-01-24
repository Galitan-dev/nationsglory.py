from nations_glory.helpers import Units, parse_duration

def test_parse_duration_simple_short():
    duration = parse_duration('6w')
    assert duration == 6 * 7 * 24 * 3600 * 1000

def test_parse_duration_simple_en():
    duration = parse_duration('8 months')
    assert duration == 8 * 28 * 24 * 3600 * 1000

def test_parse_duration_simple_fr():
    duration = parse_duration('5 jours')
    assert duration == 5 * 24 * 3600 * 1000

def test_parse_duration_complex_short():
    duration = parse_duration('5y 28d 2h 3ms')
    assert duration == 160214400003

def test_parse_duration_complex_en():
    duration = parse_duration('3 weeks, 5 days and 13 hours')
    assert duration == 2293200000

def test_parse_duration_complex_fr():
    duration = parse_duration('2 mois, 1 semaine, 8 heures et 1 seconde')
    assert duration == 5472001000