from typing import List
from src.databases.common.constants import *
from src.databases.items import Item
from src.databases.body import EatenLog
from src.common.decorators import notImplementedYet

class SQLAccess:
    @staticmethod
    @notImplementedYet
    def close_and_dispose(s=Session,e=Engine):
        """
        Closes the connection to the Database.
        For resetting, imports etc.
        """
        if s is None:
            session.close()
        else:
            s.close()
        if e is None:
            engine.dispose()
        else:
            e.dispose()
            
    @staticmethod
    def connect():
        """
        Creates a connection to the Database
        
        :return: The SessionMaker, Engine & Session
        """
        engine = create_engine(DB_URL)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session, engine, Session

class DAH:
    """
    Data Access Handler
    
    CRUD Methods for all needed Tables:
    * Item
    * EatenLog
    """
    
    @staticmethod
    def createItem(**data):
        """
        Creates an Item in the ItemTable, add to Session & commit
        """
        obj = Item(**data)
        session.add(obj)
        session.commit()
    
    @staticmethod
    def createEatenLogEntry(**data):
        """
        Creates an EatenLog in the EatenLogTable, add to Session & commit
        """
        obj = EatenLog(**data)
        session.add(obj)
        session.commit()
        
    @staticmethod
    def readEatenLogs() -> List[EatenLog]:
        """
        Reads all EatenLogs of the EatenLogTable
        
        :return: List[EatenLog]
        """
        return session.query(EatenLog).all()

    @staticmethod
    def readItems() -> List[Item]: 
        """
        Reads all Items of the ItemTable
        
        :return: List[Item]
        """
        return session.query(Item).all()
    
    @staticmethod
    @notImplementedYet
    def updateItem(id: int, **data): 
        obj = DAH.readItem(id)
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
    
    

session, engine, Session = SQLAccess.connect()