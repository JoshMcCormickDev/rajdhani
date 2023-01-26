from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from rajdhani.db_ops import Base
from rajdhani.models.train import Train

class Booking(Base):
    __tablename__ = "booking"
    
    id = Column(Integer, primary_key=True)
    train_number = Column(String, ForeignKey(Train.number))
    from_station_code = Column(String)
    to_station_code = Column(String)
    passenger_name = Column(String)
    passenger_email = Column(String)
    ticket_class = Column(String)
    date = Column(String)

    train = relationship("Train", foreign_keys=[train_number], backref="bookings")

    def get_result(self):
        return {
            "train_number": self.train_number,
            "train_name": self.train.name,
            "from_station_code": self.from_station_code,
            "from_station_name": self.train.from_station_name,
            "to_station_code": self.to_station_code,
            "to_station_name": self.train.to_station_name,
            "ticket_class": self.ticket_class,
            "date": self.date,
            "passenger_name": self.passenger_name,
            "passenger_email": self.passenger_email
        },

    def __repr__(self):
        return f"<Station {self.code}>"
