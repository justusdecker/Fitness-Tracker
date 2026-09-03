from src.databases.common.constants import ( Base, Column, String, Integer, Numeric )
from datetime import datetime 

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import declarative_base, relationship
from src.databases.data_access import session
from typing import List, Self
from datetime import datetime, timezone
class ActivityLog(Base):
    """
    # ActivityLog
    Used for tracking activitys of the User.
    
    :param id: `primary=True`
    :param activity_type: The type like e.g.: Walk, Swim, Workout
    :param duration_minutes: The duration of the activity in minutes
    :param distance_km: Walked, Runned Distance in Kilometer, is `None` if not needed
    :param steps: Walked, Runned Distance in Steps, is `None` if not needed
    :param timestamp: The timestamp of the entry of type `DateTime`
    
    """
    __tablename__ = 'activity_log'

    id = Column(Integer, primary_key=True)
    activity_type = Column(String, nullable=False)  
    duration_minutes = Column(Integer, nullable=True) 
    distance_km = Column(Float, nullable=True) 
    steps = Column(Integer, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow) #! UTCNOW is deprecated
    
class BodyMetrics(Base):
    """
    Combines all BodyMetrics at one centerpoint.
    
    !Currently no useful doc
    
    """
    __tablename__ = 'body_metrics'

    id = Column(Integer, primary_key=True)
    weight_kg = Column(Float, nullable=False)      # z. B. 95.0 (als Float statt String!)
    l_arm_size = Column(Float, nullable=True)       # z. B. 182.0
    timestamp = Column(DateTime, default=datetime.utcnow)

class EatenLog(Base):
    """
    Keep a record of which food was eaten, when, and in what quantity.
    
    :param id: `primary=True`
    :param amount: Amount in gramm, milligramm or pieces.
    :param timestamp: The timestamp of the entry of type `DateTime`
    :param item: The Link to the `Item` Table
    :param item_id: The id of the item in the `Item` Table
    """
    __tablename__ = 'eaten_log'

    id = Column(Integer, primary_key=True)
    amount = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    item = relationship("Item")
    
    #! Missing validation
    
    @staticmethod
    def create(**data):
        """
        Creates an EatenLog in the EatenLogTable, add to Session & commit
        """
        obj = EatenLog(**data)
        session.add(obj)
        session.commit()
        
    @staticmethod
    def readDateRange(start: datetime | None = None, end: datetime | None = None) -> List["EatenLog"]:
        """
        Reads EatenLogs that in the specified DateRange
        
        :return: List[EatenLog]
        """
        print(start, end)
        if start is None:
            start = datetime.now()
    
        if end is None:
            end = start
        start = start.astimezone()
        end = end.astimezone()
        start = start.replace(tzinfo=None).replace(hour=0, minute=0, second=0, microsecond=0)
        end = end.replace(tzinfo=None).replace(hour=23, minute=59, second=59, microsecond=999999)
        return session.query(EatenLog).filter(
            EatenLog.timestamp.between(start, end)
        )
    
    @staticmethod
    def read() -> List["EatenLog"]:
        """
        Reads all EatenLogs of the EatenLogTable
        
        :return: List[EatenLog]
        """
        return session.query(EatenLog).all()
    
    @staticmethod
    def delete(obj): 
        session.delete(obj)
        print(obj.timestamp)
        session.commit()