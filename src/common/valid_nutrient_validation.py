import re
from typing import Literal, Optional

# 1. Definition: allowed Modes of Literal Type
ValidationMode = Literal['mass', 'volume', 'energy', 'count']

# 2. Assignment of allowed units per mode
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
    Checks the given value:
    * Is it of type str
    * Does the unit exist
    * Does the unit match
    
    :param value: The String to check (e.g. "500mg", "1.2 g", "1,5 l", "500 kcal", "<0.1g")
    :param mode: The Mode ('mass', 'volume', 'energy', 'count')
    :return: True if the String matches the pattern (numeric[seperated_or_not])(string[mode]) else False
    """
    if value is None: return False

    if not isinstance(value, str): raise TypeError('Value must be of type str')

    trimmed = value.strip()
    if not trimmed: return False

    # Check: Is unit in the unit collection
    if mode in ALLOWED_UNITS: 
        allowed_units = ALLOWED_UNITS[mode]
    else:
        raise ValueError(f"Invalid Mode: {mode}. Allowed is: mass, volume, energy, count")

    # Create RegEx-Pattern:
    # 1. Optional Traces (< or >) with optional Spaces
    # 2. Positiv Integer or Float with dot OR Comma
    # 3. Optional Spaces
    # 4. Allowed Units OR pure Numeric
    units_pattern = '|'.join(re.escape(u) for u in allowed_units)
    pattern = rf"^(?:[<>]\s*)?\d+(?:[.,]\d+)?\s*(?:{units_pattern})?$"

    return bool(re.match(pattern, trimmed, re.IGNORECASE))