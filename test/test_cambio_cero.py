import pytest
from src.lose_change import loose_change

@pytest.mark.cambio_cero
def test_cambio_cero():
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
