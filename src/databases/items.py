from src.databases.common.constants import ( Base, Column, String, Integer, Numeric )
from src.common.valid_nutrient_validation import is_valid_nutrient_string
from src.common.unit_convert import Mass
from sqlalchemy.orm import validates
from sqlalchemy import JSON

class NutrientSet:
    
    SETNAMES = 'FETTSÄUREN_UND_ZUCKER', 'MINERALSTOFFE_SPURENELEMENTE', 'VITAMINE', 'AMINOSÄUREN', 'PERFORMANCE_SUPPLEMENTS'
    
    FETTSÄUREN_UND_ZUCKER = 'einfach_ungesaettigte_fettsaeuren', 'mehrfach_ungesaettigte_fettsaeuren', 'omega_3', 'omega_6', 'trans_fettsaeuren', 'mehrwertige_alkohole'
    
    MINERALSTOFFE_SPURENELEMENTE = 'kalium', 'kalzium', 'magnesium', 'eisen', 'zink',
    
    VITAMINE = 'A', 'E', 'K', 'C', 'D', 'B1', 'B2', 'B3', 'B5', 'B6', 'B7', 'B9', 'B12' , 'beta_carotin'

    AMINOSÄUREN = 'bcaa', 'eaas', 'l_glutamin', 'l_arginin', 'l_citrullin',
    
    PERFORMANCE_SUPPLEMENTS = 'kreatin', 'beta_alanin', 'taurin', 'koffein', 'l_carnitin', 'l_theanin', 'n_acetyl_l_tyrosin'
    
class ItemColumns:
    """
    ? Diese Tuples bilden eine Ausnahme und werden nicht zur Erstellung eines Dicts verwendet, sondern um das erstellen von ExpansionTiles zu vereinfachen
    """
    
    ESSENTIELL = 'titel', 'beschreibung', 'zutaten', 'vorschaubild', 'barcode', 'marke', 'serviermenge', 'gewicht', 'allergene', 'nova_gruppe', 'nutri_score'
    
    ERNÄHRUNGSTABELLE = 'kalorien', 'fett', 'davon_gesättigte_fettsäuren', 'kohlenhydrate', 'ballaststoffe', 'zucker', 'protein', 'salz'
    
class Item(Base):
    """
    Item-Table
    """
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    
    # 1. Essential
    titel = Column(String, nullable= False)
    beschreibung = Column(String)
    zutaten = Column(String)
    vorschaubild = Column(String)
    barcode = Column(String)
    marke = Column(String)
    serviermenge = Column(String)
    gewicht = Column(String)
    allergene = Column(String)
    nova_gruppe = Column(String)
    nutri_score = Column(String)
    # 2. Nutrition Table
    kalorien = Column(String)
    fett = Column(String)
    davon_gesättigte_fettsäuren = Column(String)
    kohlenhydrate = Column(String)
    ballaststoffe = Column(String)
    zucker = Column(String)
    protein = Column(String)
    salz = Column(String)
    # 3.Vitamines & Other
    VITAMINE = Column(JSON)
    FETTSÄUREN_UND_ZUCKER = Column(JSON)
    MINERALSTOFFE_SPURENELEMENTE = Column(JSON)
    AMINOSÄUREN = Column(JSON)
    PERFORMANCE_SUPPLEMENTS = Column(JSON)
    @validates('kalorien', 'fett', 'davon_gesättigte_fettsäuren', 'kohlenhydrate', 'ballaststoffe', 'zucker', 'protein', 'salz')
    def validate_nutrition_fields(self, key, value):
        Mass(value).get()            
        return value   
    
    @validates('VITAMINE', 'FETTSÄUREN_UND_ZUCKER', 'MINERALSTOFFE_SPURENELEMENTE', 'AMINOSÄUREN', 'PERFORMANCE_SUPPLEMENTS')
    def validate_json_fields(self, key, value):
        for k in value:
            if value[k] is None: continue
            if value[k] not in NutrientSet.VITAMINE:
                raise ValueError(f'{value[k]} is not in VITAMINE')
            Mass(value[k]).get()
            
        return value

        