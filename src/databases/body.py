from src.databases.common.constants import ( Base, Column, String, Integer, Numeric )
from datetime import datetime 

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import declarative_base, relationship


class ActivityLog(Base):
    __tablename__ = 'activity_log'

    id = Column(Integer, primary_key=True)
    activity_type = Column(String, nullable=False)  # z. B. "Gehen", "Schwimmen", "Workout"
    duration_minutes = Column(Integer, nullable=True) # z. B. 20 oder 120
    distance_km = Column(Float, nullable=True)       # z. B. 10.0
    steps = Column(Integer, nullable=True)           # z. B. 13250
    timestamp = Column(DateTime, default=datetime.utcnow)
    
class BodyMetrics(Base):
    """
    Fasst Gewicht und Körpergröße in einer Verlaufstabelle zusammen.
    Datentypen als Float/DateTime ermöglichen spätere Auswertungen (z. B. BMI-Verlauf).
    """
    __tablename__ = 'body_metrics'

    id = Column(Integer, primary_key=True)
    weight_kg = Column(Float, nullable=False)      # z. B. 95.0 (als Float statt String!)
    l_arm_size = Column(Float, nullable=True)       # z. B. 182.0
    timestamp = Column(DateTime, default=datetime.utcnow)

class EatenLog(Base):
    """
    Protokolliert, wann welches Lebensmittel in welcher Menge gegessen wurde.
    """
    __tablename__ = 'eaten_log'

    id = Column(Integer, primary_key=True)
    amount = Column(String, nullable=False)        # Menge in Gramm (z. B. 400.0 für Gratin)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Verknüpfung zur bestehenden Ernährungs-Datenbank
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    item = relationship("Item")