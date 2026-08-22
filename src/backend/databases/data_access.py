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
    
    @staticmethod
    def delete_letsplay(lpid: int):
        """
        Deletes a letsplay and all its associated episodes.
        
        Args:
            lpid (int): The index of the letsplay to delete.
        """
        data = session.query(LetsPlays).all()[lpid]
        session.delete(data)
        while SQLAccess.read_episodes(lpid):
            SQLAccess.delete_episode(lpid, 0)
        session.commit()

class DAH:
    """
    Data Access Handler
    """
    def createItem():
        data = Item(**vars)
        session.add(data)
        session.commit()
    def readItem(): ...
    def updateItem(): ...
    def deleteItem(): ...
    
    

session, engine, Session = SQLAccess.connect()