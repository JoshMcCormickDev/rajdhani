from sqlalchemy import Column, String, Integer

from rajdhani.db_ops import Base

class Schedule(Base):
    __tablename__ = "schedule"
    
    station_code = Column(String, primary_key=True)
    station_name = Column(String)
    train_number = Column(String)
    train_name = Column(String)
    day = Column(Integer)
    arrival = Column(String)    
    departure = Column(String)

    def get_result(self):
        return {
            "station_code": self.station_code,
            "station_name": self.station_name,
            "day": self.day,
            "arrival": self.arrival,
            "departure": self.departure
        }

    def __repr__(self):
        return f"<Station {self.code}>"
