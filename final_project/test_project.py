import pytest
from project import (
    calculate_decay,
    calculate_shielding,
    calculate_reactivity,
    calculate_energy,
)


def test_calculate_decay():
    assert calculate_decay(100, 5, 5) == 50.0
    assert calculate_decay(100, 5, 10) == 25.0
    assert calculate_decay(100, 5, 0) == 100.0
    with pytest.raises(ValueError):
        calculate_decay(-10, 5, 5)
    with pytest.raises(ValueError):
        calculate_decay(100, 0, 5)


def test_calculate_shielding():
    assert calculate_shielding(100, 0.772, 0) == 100.0
    assert calculate_shielding(100, 0.5, 2) == 36.7879
    with pytest.raises(ValueError):
        calculate_shielding(-10, 0.5, 2)
    with pytest.raises(ValueError):
        calculate_shielding(100, 0, 2)


def test_calculate_reactivity():
    assert calculate_reactivity(1.0) == {"rho": 0.0, "state": "CRITICAL"}
    assert calculate_reactivity(1.25) == {"rho": 0.2, "state": "SUPERCRITICAL"}
    assert calculate_reactivity(0.8) == {"rho": -0.25, "state": "SUBCRITICAL"}
    with pytest.raises(ValueError):
        calculate_reactivity(0)


def test_calculate_energy():
    assert calculate_energy(0) == 0.0
    assert calculate_energy(1) == 89875517.87
    with pytest.raises(ValueError):
        calculate_energy(-5)
