from src.common.valid_nutrient_validation import is_valid_nutrient_string
# --- MODUS: MASS (Gewicht) ---
print(is_valid_nutrient_string("500mg", "mass"))       # True
print(is_valid_nutrient_string("1.2 g", "mass"))       # True
print(is_valid_nutrient_string("0,5kg", "mass"))       # True (Komma akzeptiert)
print(is_valid_nutrient_string("< 0.1g", "mass"))      # True (Spuren-Angaben)
print(is_valid_nutrient_string("500ml", "mass"))       # False (ml gehört zu Volumen!)
print(is_valid_nutrient_string("-10g", "mass"))        # False (keine negativen Werte)

# --- MODUS: VOLUME (Flüssigkeiten) ---
print(is_valid_nutrient_string("250 ml", "volume"))    # True
print(is_valid_nutrient_string("1,5 l", "volume"))     # True
print(is_valid_nutrient_string("500g", "volume"))      # False

# --- MODUS: ENERGY (Kalorien) ---
print(is_valid_nutrient_string("536 kcal", "energy"))  # True
print(is_valid_nutrient_string("2100 kJ", "energy"))   # True
print(is_valid_nutrient_string("500 g", "energy"))     # False

# --- MODUS: COUNT (Portionen) ---
print(is_valid_nutrient_string("1 Serving", "count"))  # True
print(is_valid_nutrient_string("2 Kapseln", "count"))  # True

# --- REINE ZAHLEN (Ohne Suffix) ---
print(is_valid_nutrient_string("500", "any"))          # True (Nützlich für reine Zahlen-Eingaben)
print(is_valid_nutrient_string("Ungültig", "any"))     # False