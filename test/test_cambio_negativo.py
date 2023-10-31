import pytest
from src.lose_change import loose_change

@pytest.mark.cambio_negativo
def test_cambio_negativo():
    assert loose_change(-98) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
