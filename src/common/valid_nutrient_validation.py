import re
from typing import Literal, Optional

# 1. Definition der erlaubten Modi als Literal Type
ValidationMode = Literal['mass', 'volume', 'energy', 'count']

# 2. Zuordnung der erlaubten Einheiten pro Modus
ALLOWED_UNITS: dict[str, list[str]] = {
    'mass': ['g', 'mg', 'mcg', 'µg', 'ug', 'kg', 'ng'],
    'volume': ['l', 'ml', 'dl', 'cl'],
    'energy': ['kcal', 'kj', 'cal'],
    'count': [
        'stk', 'stück', 'stk.', 'serving', 'servings', 'portion', 
        'portionen', 'kapsel', 'kapseln', 'becher', 'dose', 'dosen', 'tl', 'el'
    ]
}

def is_valid_nutrient_string(value: Optional[str], mode: ValidationMode) -> bool:
    """
    Prüft, ob ein Nährwert-String für den angegebenen Modus gültig ist.
    
    :param value: Der zu prüfende String (z. B. "500mg", "1.2 g", "1,5 l", "500 kcal", "<0.1g")
    :param mode: Der Modus ('mass', 'volume', 'energy', 'count')
    :return: True wenn der String dem Muster entspricht, sonst False
    """
    if value is None:
        return False

    # Falls versehentlich ein int oder float übergeben wird, in String umwandeln
    if isinstance(value, (int, float)):
        value = str(value)

    trimmed = value.strip()
    if not trimmed:
        return False

    # Erlaubte Einheiten ermitteln

    if mode in ALLOWED_UNITS:
        allowed_units = ALLOWED_UNITS[mode]
    else:
        raise ValueError(f"Ungültiger Modus: {mode}. Erlaubt sind: mass, volume, energy, count")

    # RegEx-Pattern erstellen:
    # 1. Optionales Spuren-Zeichen (< oder >) mit optionalen Leerzeichen
    # 2. Positiver Integer oder Float mit Punkt ODER Komma
    # 3. Optionale Leerzeichen
    # 4. Erlaubte Einheiten ODER reine Zahl (Einheit optional)
    units_pattern = '|'.join(re.escape(u) for u in allowed_units)
    pattern = rf"^(?:[<>]\s*)?\d+(?:[.,]\d+)?\s*(?:{units_pattern})?$"

    return bool(re.match(pattern, trimmed, re.IGNORECASE))