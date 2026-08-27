from src.databases.common.constants import ( Base, Column, String, Integer, Numeric )
class Item(Base):
    """
    Item-Table
    
    Alle Werte angegeben in gramm auf 100gramm.
    """
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    
    title = Column(String, nullable= False)
    description = Column(String)
    ingredients = Column(String)
    img = Column(String)
    
    calorific_value = Column(Numeric)
    fat = Column(Numeric)
    saturated_fatty_acids = Column(Numeric)
    carbohydrates = Column(Numeric)
    protein = Column(Numeric)
    salt = Column(Numeric)
    
    vitamine_D = Column(Numeric)
    vitamine_C = Column(Numeric)
    vitamine_B1 = Column(Numeric)
    vitamine_B2 = Column(Numeric)
    vitamine_B3 = Column(Numeric)
    vitamine_B5 = Column(Numeric)
    vitamine_B6 = Column(Numeric)
    vitamine_B7 = Column(Numeric)
    vitamine_B9 = Column(Numeric)
    vitamine_B12 = Column(Numeric)
    
    beta_alanine = Column(Numeric)
    creatine = Column(Numeric)
    magnesium = Column(Numeric)
    n_acetyl_l_tyrosin = Column(Numeric)
    l_arginin = Column(Numeric)
    l_citrullin = Column(Numeric)
    caffeine = Column(Numeric)
    
    nutri_score = Column(Integer)
    
    
    
    @staticmethod
    def getVarTable():
        return [
            'title',
            'description',
            'img',
            'calorific_value',
            'fat',
            'saturated_fatty_acids',
            'carbohydrates',
            'protein',
            'salt',
            'vitamine_D',
            'vitamine_C',
            'vitamine_B1',
            'vitamine_B2',
            'vitamine_B3',
            'vitamine_B5',
            'vitamine_B6',
            'vitamine_B7',
            'vitamine_B9',
            'vitamine_B12',
            'beta_alanine',
            'creatine',
            'magnesium',
            'n_acetyl_l_tyrosin',
            'l_arginin',
            'l_citrullin',
            'caffeine',
            'nutri_score',
            'ingredients'
        ]
    @staticmethod
    def getVarTableCropped():
        t = Item.getVarTable()
        t.remove('img')
        t.remove('title')
        t.remove('description')
        t.remove('ingredients')
        return t