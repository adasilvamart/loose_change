import pytest
from src.lose_change import loose_change

@pytest.mark.cambio_decenas_positivo
def test_cambio_entero_decenas_positivo():
    assert loose_change(56) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}