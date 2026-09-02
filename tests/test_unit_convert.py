
from src.common.unit_convert import Mass
import pytest
from unittest.mock import patch

@pytest.fixture(autouse=True)
def mock_nutrient_validation():
    with patch("src.common.valid_nutrient_validation.is_valid_nutrient_string", return_value=True):
        yield


class TestMassOperators:
    """Tests for arithmetic Operators (+, -, *, /) with Mass and Numbers."""

    def test_addition_with_mass_and_numeric(self):
        m1 = Mass("500mg")
        m2 = Mass("0.5g")
        
        res1 = m1 + m2
        assert str(res1) == "1g"

        res2 = m1 + 0.5
        assert str(res2) == "1g"

    def test_subtraction_with_mass_and_numeric(self):
        m1 = Mass("1kg")
        m2 = Mass("200g")
        
        assert str(m1 - m2) == "800g"
        assert str(m1 - 200) == "800g"

    def test_multiplication_correct_math(self):
        m = Mass("250mg")
        res = m * 4
        assert str(res) == "1g"

    def test_division_correct_math(self):
        m = Mass("1g")
        res = m / 2
        assert str(res) == "500mg"

    def test_invalid_type_raises_type_error(self):
        m = Mass("100g")
        with pytest.raises(TypeError):
            _ = m + "invalid_string"

    def test_trace_propagation(self):
        m1 = Mass("< 100mg")
        m2 = Mass("200mg")
        res = m1 + m2
        assert res.has_traces is True


class TestMassGetInstanceMethod:
    """Tests for the get()-Instancemethod."""

    def test_get_with_explicit_units(self):
        m = Mass("1000g")
        assert m.get("kg") == "1kg"
        assert m.get("g") == "1000g"
        assert m.get("mg") == "1000000mg"

    def test_get_auto_formatting(self):
        assert Mass("1000g").get("auto") == "1kg"
        assert Mass("1.5g").get("auto") == "1.5g"
        assert Mass("0.001g").get("auto") == "1mg"

    def test_get_invalid_unit_raises_value_error(self):
        m = Mass("100g")
        with pytest.raises(KeyError):
            m.get("invalid_unit")