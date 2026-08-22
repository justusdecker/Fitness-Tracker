from src.backend.databases.common.constants import ( Base, Column, String, Integer )
class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    
    
    tad_path = Column(String)
    
    name = Column(String)
    game_name = Column(String)
    episode_length = Column(Integer)
    description_path = Column(String)
    jitle = Column(String)
    emoji = Column(String)
    
    @staticmethod
    def getVarTable():
        return ...