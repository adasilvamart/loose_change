from src.lose_change import loose_change

def test_cambio_cero():
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

def test_cambio_entero_decenas_positivo():
    assert loose_change(56) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}

def test_cambio_negativo():
    assert loose_change(-98) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

# Descomentar para ver un test erroneo
# def test_erroneo():
#   assert loose_change(12) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}