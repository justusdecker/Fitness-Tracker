from src.common.valid_nutrient_validation import is_valid_nutrient_string
from typing import Literal
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
        if not is_valid_nutrient_string(val):
            raise TypeError()

        self.__convert2GrammAndNumeric(val)

    def __convert2GrammAndNumeric(self, val: str):
        for mf in MASS_FACTORS:
            if val.endswith(mf): 
                i = MASS_FACTORS.index(mf)
                self.weight = float(val.replace(mf, '')) * MASS[i][1]
                break
        else:
            raise NotImplementedError()
    
    def calc(self, other: MassLike, _resType: MassResultType):
        i = MASS_FACTORS.index(_resType)
        print(i, MASS_FACTORS[i])
        if _resType == 'kg':
            return (self.weight + other.weight) * MASS[i][1]
        else:
            return (self.weight + other.weight) / MASS[i][1]
        
        
    def get(self, _resType: MassResultType = 'g'):
        i = MASS_FACTORS.index(_resType)
        
        if _resType == 'kg':
            weight = self.weight * MASS[i][1]
        else:
            weight = self.weight / MASS[i][1]
        return f'{weight}{_resType}'


a = Mass('10kg')
b = Mass('2000g')
print(a.get('ng'), b.get('mg'))
print(a.calc(b, 'mg'))