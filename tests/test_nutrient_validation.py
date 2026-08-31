from src.common.valid_nutrient_validation import is_valid_nutrient_string
import pytest as pt
def test_ivns():
    
    # --- MODUS: MASS (Gewicht) ---
    assert is_valid_nutrient_string("500mg", "mass")
    assert is_valid_nutrient_string("1.2 g", "mass")
    assert is_valid_nutrient_string("0,5kg", "mass") # Komma
    assert is_valid_nutrient_string("< 0.1g", "mass") # Spurenangaben
    assert not is_valid_nutrient_string("500ml", "mass") # ml -> Volume != mass
    assert not is_valid_nutrient_string("-10g", "mass") # keine negativen Werte
    # --- MODUS: VOLUME (Flüssigkeiten) ---
    assert is_valid_nutrient_string("250 ml", "volume")
    assert is_valid_nutrient_string("1,5 l", "volume")
    assert not is_valid_nutrient_string("500g", "volume")
    # --- MODUS: ENERGY (Kalorien) ---
    assert is_valid_nutrient_string("536 kcal", "energy")
    assert is_valid_nutrient_string("2100 kJ", "energy")
    assert not is_valid_nutrient_string("500 g", "energy")
    # --- MODUS: COUNT (Portionen) ---
    assert is_valid_nutrient_string("1 Serving", "count")
    assert is_valid_nutrient_string("2 Kapseln", "count")
    # --- REINE ZAHLEN (Ohne Suffix) ---
    with pt.raises(ValueError):
        is_valid_nutrient_string("500", "test")
    
    with pt.raises(TypeError):
        is_valid_nutrient_string('123')