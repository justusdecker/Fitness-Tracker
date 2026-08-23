from src.backend.databases.common.constants import ( Base, Column, String, Integer, Numeric )
class Item(Base):
    """
    Item-Table
    
    Alle Werte angegeben in gramm auf 100gramm.
    """
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    
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
    caffeine = Column(Numeric)
    
    nutri_score = Column(Integer)
    
    @staticmethod
    def getVarTable():
        return ...