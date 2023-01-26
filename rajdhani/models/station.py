from sqlalchemy import Column, String, Float, and_, or_, func
from sqlalchemy.orm import relationship

from rajdhani.db_ops import Base


# =======================================================================
class Station(Base):
    __tablename__ = "station"
    
    code = Column(String, primary_key=True)
    name = Column(String)
    zone = Column(String)
    state = Column(String)
    address = Column(String)
    latitude = Column(Float)    
    longitude = Column(Float)

    @staticmethod
    def matches_search(search):
        matches_code = func.lower(Station.code).startswith(search.lower())
        matches_name = func.lower(Station.name).contains(search.lower())
        return or_(matches_code, matches_name)

    def get_result(self):
        return {
            "code": self.code,
            "name": self.name
        }
    

    def __repr__(self):
        return f"<Station {self.code}>"
