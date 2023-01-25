from . import db_ops
db_ops.ensure_db()

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base(bind=db_ops.engine)

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


class Train(Base):
    __tablename__ = "train"
    
    number = Column(String, primary_key=True)
    name = Column(String)
    type = Column(String)
    zone = Column(String)
    from_station_code = Column(String, ForeignKey(Station.code))
    from_station_name = Column(String)
    to_station_code = Column(String, ForeignKey(Station.code))
    to_station_name = Column(String)
    departure = Column(String)
    arrival = Column(String)
    duration_h = Column(Float)
    duration_m = Column(Float)
    distance = Column(Float)
    return_train = Column(String)
    sleeper = Column(Integer)
    third_ac = Column(Integer)
    second_ac = Column(Integer)
    first_ac = Column(Integer)
    first_class = Column(Integer)
    chair_car = Column(Integer)
    
    from_station = relationship("Station", 
                                foreign_keys=[from_station_code],
                                backref="starting_trains")
    to_station = relationship("Station", 
                                foreign_keys=[to_station_code],
                                backref="terminating_trains")
    
    def __repr__(self):
        return f"<Train {self.number}>"  


# class Booking(Base):
#     __tablename__ = "booking"
    
#     id = Column(Integer, primary_key=True)
#     train_number = Column(String, ForeignKey(Train.number))

#     from_station_code = Column(String, ForeignKey(Station.code))
#     to_station_code = Column(String, ForeignKey(Station.code))

#     passenger_name = Column(String)
#     passenger_email = Column(String)
#     ticket_class = Column(String)
#     date = Column(String)
    
#     train = relationship("Train", foreign_keys=[train_number], backref="bookings")
#     from_station = relationship("Station", 
#                                 foreign_keys=[from_station_code],
#                                 backref="starting_trains")
#     to_station = relationship("Station", 
#                                 foreign_keys=[to_station_code],
#                                 backref="terminating_trains")
    
#     def __repr__(self):
#         return f"<Booking {self.id}>"
