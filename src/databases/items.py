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
    barcode = Column(String)
    brand = Column(String)
    
    
    calorific_value = Column(String)
    fat = Column(String)
    saturated_fatty_acids = Column(String)
    carbohydrates = Column(String)
    fiber = Column(String)
    sugar = Column(String)
    protein = Column(String)
    salt = Column(String)
    
    unsaturated_fatty_acids = Column(String)
    monounsaturated_fat = Column(String)
    polyunsaturated_fat = Column(String)
    omega_3 = Column(String)
    omega_6 = Column(String)
    trans_fat = Column(String)
    polyols = Column(String)
    vitamine_A = Column(String)
    beta_carotine = Column(String)
    vitamine_E = Column(String)
    vitamine_K = Column(String)
    zinc = Column(String)
    iron = Column(String)
    potassium = Column(String)
    sodium = Column(String)
    bcaa = Column(String)
    eaas = Column(String)
    l_glutamine = Column(String)
    l_carnitine = Column(String)
    taurine = Column(String)
    l_theanine = Column(String)
    serving_size = Column(String)
    net_weight = Column(String)
    allergens = Column(String)
    nova_group = Column(String)
    
    vitamine_D = Column(String)
    vitamine_C = Column(String)
    vitamine_B1 = Column(String)
    vitamine_B2 = Column(String)
    vitamine_B3 = Column(String)
    vitamine_B5 = Column(String)
    vitamine_B6 = Column(String)
    vitamine_B7 = Column(String)
    vitamine_B9 = Column(String)
    vitamine_B12 = Column(String)
    
    beta_alanine = Column(String)
    creatine = Column(String)
    magnesium = Column(String)
    n_acetyl_l_tyrosin = Column(String)
    l_arginin = Column(String)
    l_citrullin = Column(String)
    caffeine = Column(String)
    calcium = Column(String)
    
    nutri_score = Column(String)
    
    @staticmethod
    def getVarTable():
        return [
            'title',
            'description',
            'img',
            'barcode',
            'brand',
            'calorific_value',
            'fat',
            'saturated_fatty_acids',
            'carbohydrates',
            'sugar',
            'fiber',
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
            'calcium',
            'nutri_score',
            'ingredients',
            "unsaturated_fatty_acids",
            "monounsaturated_fat",
            "polyunsaturated_fat",
            "omega_3",
            "omega_6",
            "trans_fat",
            "polyols",
            "vitamine_A",
            "beta_carotine",
            "vitamine_E",
            "vitamine_K",
            "zinc",
            "iron",
            "potassium",
            "sodium",
            "bcaa",
            "eaas",
            "l_glutamine",
            "l_carnitine",
            "taurine",
            "l_theanine",
            "serving_size",
            "net_weight",
            "allergens",
            "nova_group",
        ]
    @staticmethod
    def getVarTableCropped():
        t = Item.getVarTable()
        t.remove('img')
        t.remove('title')
        t.remove('description')
        t.remove('ingredients')
        return t