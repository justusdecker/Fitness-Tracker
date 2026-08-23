from src.backend.databases.common.constants import *
from src.backend.databases.items import Item
class SQLAccess:
    @staticmethod
    def close_and_dispose(s=None,e=None):
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
        engine = create_engine(DB_URL)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session, engine, Session

class DAH:
    """
    Data Access Handler
    """
    def createItem(**data):
        obj = Item(**data)
        session.add(obj)
        session.commit()
    
    
    
    def readItems(): 
        return session.query(Item).all()
        
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
            
    def deleteItem(id: int): 
        data = session.query(Item).all()[id] #! optimize
        session.delete(data)
        session.commit()
    
    

session, engine, Session = SQLAccess.connect()