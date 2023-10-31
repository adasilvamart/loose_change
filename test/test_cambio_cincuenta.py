import pytest
from src.lose_change import loose_change

@pytest.mark.cambio_cincuenta
def test_cambio_cincuenta():
    assert loose_change(100) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 4}