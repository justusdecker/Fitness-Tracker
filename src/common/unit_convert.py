from src.common.valid_nutrient_validation import is_valid_nutrient_string
from typing import Literal
import re
MASS = (
    ('kg', 10**3),
    ('g', 1),
    ('mg', 10**-3),
    ('µg', 10**-6),
    ('ng', 10**-9)
)
MASS_FACTORS = 'kg', 'g', 'mg', 'µg', 'ng'


type MassResultType = Literal['kg'] | Literal['g'] | Literal['mg'] | Literal['µg'] | Literal['ng']
class MassLike: 
    weight: float = ...



class Mass:
    def __init__(self, val: str):
        if not is_valid_nutrient_string(val, 'mass'):
            raise TypeError(f'{val} is not valid, must be of type mass')

        self.__convert2GrammAndNumeric(val)

    def __convert2GrammAndNumeric(self, val: str):
        MD = dict(MASS)
        # 1. Leerzeichen entfernen und Strings wie "1.5 kg" oder "1,5kg" normieren
        val_clean = str(val).strip().replace(',', '.')
        
        # 2. Per Regex Zahl und Einheit sauber trennen
        match = re.match(r"^([+-]?\d*(?:\.\d+)?)\s*([a-zA-Zµ]+)$", val_clean)
        
        if not match:
            raise ValueError(f"Ungültiges Format für Gewichtsangabe: '{val}'")
            
        num_str, unit = match.groups()
        
        if unit not in MD:
            raise ValueError(f"Unbekannte Einheit '{unit}'. Erlaubt sind: {list(MD.keys())}")
            
        # 3. Umrechnung in Basis-Gramm (Zahl * Faktor)
        self.weight = float(num_str) * MD[unit]
    
    def calc(self, other: MassLike, _resType: MassResultType):
        if _resType not in MASS_FACTORS:
            raise NameError(f'{_resType} does not exist in here')
        if not isinstance(other, Mass):
            raise TypeError('Incompatible Calc')
        i = MASS_FACTORS.index(_resType)
        if _resType == 'kg':
            return (self.weight + other.weight) * MASS[i][1]
        else:
            return (self.weight + other.weight) / MASS[i][1]
        
        
    def get(self, _resType: str = 'auto') -> str:
        if _resType not in list(MASS_FACTORS) + ['auto']:
            raise NameError(f'{_resType} does not exist in here')
        
        # 1. Base weight in grams (assuming self.weight is in grams)
        base_g = self.weight  

        # 2. Auto-select unit with best visibility
        if _resType == 'auto':
            _resType = 'ng'  # Fallback for extremely small values
            for unit, factor in MASS:
                val = base_g / factor
                if val >= 1.0:
                    _resType = unit
                    break

        # 3. Calculate converted weight
        factor = dict(MASS).get(_resType, 1)
        weight = base_g / factor

        # 4. Format cleanly (removes trailing .0 for whole numbers)
        formatted_weight = f"{weight:.3f}".rstrip('0').rstrip('.') if isinstance(weight, float) else weight
        return f"{formatted_weight}{_resType}"
