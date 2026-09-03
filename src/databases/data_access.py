from src.databases.common.constants import *
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
        Session = sessionmaker(bind=engine)
        session = Session()
        return session, engine, Session

session, engine, Session = SQLAccess.connect()