from sqlalchemy import Column, Integer, String, Float, ForeignKey, and_, or_
from sqlalchemy.orm import relationship

from rajdhani.db_ops import Base


class Station(Base):
    __tablename__ = "station"
    
    code = Column(String, primary_key=True)
    name = Column(String)
    zone = Column(String)
    state = Column(String)
    address = Column(String)
    latitude = Column(Float)    
    longitude = Column(Float)
    
    def __repr__(self):
        return f"<Station {self.code}>"

