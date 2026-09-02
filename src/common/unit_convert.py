from src.common.valid_nutrient_validation import is_valid_nutrient_string
from typing import Literal

type Numeric = float | int
import re
MASS = (
    ('kg', 10**3),
    ('g', 1),
    ('mg', 10**-3),
    ('µg', 10**-6),
    ('ng', 10**-9)
)
MASS_FACTORS = 'kg', 'g', 'mg', 'µg', 'ng'
MASS_LIST = list(MASS_FACTORS) + ['auto']

type MassResultType = Literal['kg', 'g', 'mg', 'µg', 'ng']

class Mass:
    """
    This class is used to easy interact with masses like e.g.: **kg** and **g**
    
    Currently only Addition of two Mass-Classes is allowed
    
    You can get the Mass in you wanted Factory with `get()`
    """
    def __init__(self, val: str):
        if not is_valid_nutrient_string(val, 'mass'):
            raise TypeError(f'{val} is not valid, must be of type mass')

        self.__convert2GrammAndNumeric(val)

    def __convert2GrammAndNumeric(self, val: str):
        """
        Removes Spaces, Norms **,** to **.**, Calculates back to gramm and Set the `self.weight` property.
        
        The unit will not be stored!
        """
        MD = dict(MASS)
        
        self.has_traces = val.startswith(('<', '>')) # TODO: Give it a use. 
        
        val_clean = str(val).replace(',', '.').replace('<', '').replace('>', '').strip()
        
        match = re.match(r"^([+-]?\d*(?:\.\d+)?)\s*([a-zA-Zµ]+)$", val_clean)
        
        if not match:
            raise ValueError(f"Invalid Format for Mass: '{val}' : '{val_clean}' ")
            
        num_str, unit = match.groups()
        
        if unit not in MD:
            raise ValueError(f"Unknown unit: '{unit}'. Allowed units: {list(MD.keys())}")

        self.weight = float(num_str) * MD[unit]
    
    def __calcCheckAndGetNewMass(self, obj: "Mass") -> "Mass":
        if not isinstance(obj, (Mass, int, float)):
            raise TypeError(f'[{obj}] is not of type Mass')
        res = Mass.__new__(Mass)
        res.has_traces = self.has_traces or (obj.has_traces if isinstance(obj, Mass) else False)
        return res
    
    def __add__(self, other: "Mass | Numeric") -> "Mass":
        res = self.__calcCheckAndGetNewMass(other)
        res.weight = self.weight + (other.weight if isinstance(other, Mass) else other)
        return res

    def __sub__(self, other: "Mass | Numeric") -> "Mass":
        res = self.__calcCheckAndGetNewMass(other)
        res.weight = self.weight - (other.weight if isinstance(other, Mass) else other)
        return res

    def __mul__(self, other: "Mass | Numeric") -> "Mass":
        res = self.__calcCheckAndGetNewMass(other)
        res.weight = self.weight * (other.weight if isinstance(other, Mass) else other)
        return res

    def __truediv__(self, other: "Mass | Numeric") -> "Mass":
        res = self.__calcCheckAndGetNewMass(other)
        res.weight = self.weight / (other.weight if isinstance(other, Mass) else other)
        return res
    
    def __str__(self):
        return self.get('auto')
  
    def get(self, _resType: str = 'auto') -> str:
        """
        Get the `self.weight` property in the ResultType you want.
        """
        if _resType not in MASS_LIST:
            raise KeyError(f'{_resType} does not exist in here')
        
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
