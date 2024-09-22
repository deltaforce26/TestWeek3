import pytest
from services.calc_service import atr_calc


def test_atr_calc():
    assert atr_calc(82, 84) == 0.98
    assert atr_calc(0, 84) == 0



def test_ppg_ratio_calc():
    pass
