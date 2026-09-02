from src.databases.common.constants import ( Base, Column, String, Integer, Numeric )
from src.common.unit_convert import Mass
from sqlalchemy.orm import validates
from sqlalchemy import JSON
from src.common.decorators import notImplementedYet
from src.databases.data_access import session
from typing import List, Self

class NutrientSet:
    """
    Used for UI building, Data-Fetching etc.
    
    :param SETNAMES: Consists of the sub-nutrient names
    :type SETNAMES: tuple[Literal[str]]
    :param FETTSÄUREN_UND_ZUCKER: ...
    :type FETTSÄUREN_UND_ZUCKER: tuple[Literal[str]]
    :param MINERALSTOFFE_SPURENELEMENTE: ...
    :type MINERALSTOFFE_SPURENELEMENTE: tuple[Literal[str]]
    :param VITAMINE: ...
    :type VITAMINE: tuple[Literal[str]]
    :param AMINOSÄUREN: ...
    :type AMINOSÄUREN: tuple[Literal[str]]
    :param PERFORMANCE_SUPPLEMENTS: ...
    :type PERFORMANCE_SUPPLEMENTS: tuple[Literal[str]]
    """
    SETNAMES = 'FETTSÄUREN_UND_ZUCKER', 'MINERALSTOFFE_SPURENELEMENTE', 'VITAMINE', 'AMINOSÄUREN', 'PERFORMANCE_SUPPLEMENTS'
    
    FETTSÄUREN_UND_ZUCKER = 'einfach_ungesaettigte_fettsaeuren', 'mehrfach_ungesaettigte_fettsaeuren', 'omega_3', 'omega_6', 'trans_fettsaeuren', 'mehrwertige_alkohole'
    
    MINERALSTOFFE_SPURENELEMENTE = 'kalium', 'kalzium', 'magnesium', 'eisen', 'zink',
    
    VITAMINE = 'A', 'E', 'K', 'C', 'D', 'B1', 'B2', 'B3', 'B5', 'B6', 'B7', 'B9', 'B12' , 'beta_carotin'

    AMINOSÄUREN = 'bcaa', 'eaas', 'l_glutamin', 'l_arginin', 'l_citrullin',
    
    PERFORMANCE_SUPPLEMENTS = 'kreatin', 'beta_alanin', 'taurin', 'koffein', 'l_carnitin', 'l_theanin', 'n_acetyl_l_tyrosin'
    
class ItemColumns:
    """
    :param ESSENTIELL: Consists of the essential keys for the `Item` Table
    :type ESSENTIELL: tuple[Literal[str]]
    :param ERNÄHRUNGSTABELLE: Consists of the nutrient names
    :type ERNÄHRUNGSTABELLE: tuple[Literal[str]]
    
    ? Diese Tuples bilden eine Ausnahme und werden nicht zur Erstellung eines Dicts verwendet, sondern um das erstellen von ExpansionTiles zu vereinfachen
    """
    
    ESSENTIELL = 'titel', 'beschreibung', 'zutaten', 'vorschaubild', 'barcode', 'marke', 'serviermenge', 'gewicht', 'allergene', 'nova_gruppe', 'nutri_score'
    
    ERNÄHRUNGSTABELLE = 'kalorien', 'fett', 'davon_gesättigte_fettsäuren', 'kohlenhydrate', 'ballaststoffe', 'zucker', 'protein', 'salz'
    
class Item(Base):
    """
    Item-Table used for showing / calculating the amount of calories and more
    
    :param id: `primary=True`
    :type id: Column(Integer)
    :param titel: The title of the Item
    :type titel: Column(String)
    :param beschreibung: The description of the Item
    :type beschreibung: Column(String)
    :param zutaten: The ingredients of the Item
    :type zutaten: Column(String)
    :param vorschaubild: The img of the Item
    :type vorschaubild: Column(String)
    :param barcode: The barcode-text of the Item
    :type barcode: Column(String)
    :param marke: The brand of the Item
    :type marke: Column(String)
    :param serviermenge: The serving size of the Item in (g, mg, piece, stk)...
    :type serviermenge: Column(String)
    :param gewicht: The weight of the Item
    :type gewicht: Column(String)
    :param allergene: The allergens of the Item
    :type allergene: Column(String)
    :param nova_gruppe: The nova_group of the Item
    :type nova_gruppe: Column(String)
    :param nutri_score: The nutri_score of the Item
    :type nutri_score: Column(String)
    :param kalorien: The calories of the Item
    :type kalorien: Column(String)
    :param fett: The fat of the Item
    :type fett: Column(String)
    :param davon_gesättigte_fettsäuren: The saturated fatty acids of the Item
    :type davon_gesättigte_fettsäuren: Column(String)
    :param kohlenhydrate: The carbohydrates of the Item
    :type kohlenhydrate: Column(String)
    :param ballaststoffe: The fiber of the Item
    :type ballaststoffe: Column(String)
    :param zucker: The sugar of the Item
    :type zucker: Column(String)
    :param protein: The protein of the Item
    :type protein: Column(String)
    :param salz: The salt of the Item
    :type salz: Column(String)
    :param VITAMINE: The vitamines of the Item
    :type VITAMINE: Column(JSON)
    :param FETTSÄUREN_UND_ZUCKER: The FATTY ACIDS AND SUGAR of the Item
    :type FETTSÄUREN_UND_ZUCKER: Column(String)
    :param MINERALSTOFFE_SPURENELEMENTE: The MINERALS_TRACE ELEMENTS of the Item
    :type MINERALSTOFFE_SPURENELEMENTE: Column(String)
    :param AMINOSÄUREN: The AMINO ACIDS of the Item
    :type AMINOSÄUREN: Column(String)
    :param PERFORMANCE_SUPPLEMENTS: The PERFORMANCE_SUPPLEMENTS of the Item
    :type PERFORMANCE_SUPPLEMENTS: Column(String)
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
    def validate_nutrition_fields(self, key, value) -> str:
        """
        Validates the NutritionTable
        """
        if value is None: return value
        Mass(value).get()            
        return value   
    
    @validates('VITAMINE', 'FETTSÄUREN_UND_ZUCKER', 'MINERALSTOFFE_SPURENELEMENTE', 'AMINOSÄUREN', 'PERFORMANCE_SUPPLEMENTS')
    def validate_json_fields(self, key, value) -> str:
        """
        Validates the SubNutritionTable
        """
        for k in value:
            if value[k] is None: continue
            if value[k] not in NutrientSet.VITAMINE:
                raise ValueError(f'{value[k]} is not in VITAMINE')
            Mass(value[k]).get()
            
        return value

    @staticmethod
    def create(**data):
        """
        Creates an Item in the ItemTable, add to Session & commit
        """
        obj = Item(**data)
        session.add(obj)
        session.commit()
    
    @staticmethod
    def read() -> List["Item"]: 
        """
        Reads all Items of the ItemTable
        
        :return: List[Item]
        """
        return session.query(Item).all()
    
    @staticmethod
    @notImplementedYet
    def updateItem(id: int, **data): 
        obj = Item.readItem(id)
        for key in data:
            if not hasattr(obj, key):
                raise NameError(f'The attribute: [{key}] does not exist!')
            setattr(
                obj,
                key,
                data[key]
            )
    
    @staticmethod
    @notImplementedYet
    def deleteItem(id: int): 
        data = session.query(Item).all()[id] #! optimize
        session.delete(data)
        session.commit()