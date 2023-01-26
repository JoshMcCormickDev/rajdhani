from sqlalchemy import Column, Integer, String, Float, ForeignKey, and_, or_
from sqlalchemy.orm import relationship

from rajdhani.db_ops import Base
from rajdhani.models.station import Station

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

    _ticket_class_columns = {
        "SL": sleeper,
        "3A": third_ac,
        "2A": second_ac,
        "1A": first_ac,
        "FC": first_class,
        "CC": chair_car
    }

    _time_slots = {
        "slot1": ("00:00:00", "08:00:00"),
        "slot2": ("08:00:00", "12:00:00"),
        "slot3": ("12:00:00", "16:00:00"),
        "slot4": ("16:00:00", "20:00:00"),
        "slot5": ("20:00:00", "24:00:00"),
    }

    @staticmethod
    def is_ticket_class(ticket_class):
        if ticket_class:
            return Train._ticket_class_columns[ticket_class] == 1
        else:
            return True

    @staticmethod
    def is_in_time_slots(departure_slots, arrival_slots):
        return and_(
            Train._is_in_time_slots_inner(Train.departure, departure_slots),
            Train._is_in_time_slots_inner(Train.arrival, arrival_slots)
        )

    @staticmethod
    def _is_in_time_slots_inner(column, slots):
        if slots:
            time_slot_clauses = []
            for slot in slots:
                slot_start, slot_end = Train._time_slots[slot]
                time_slot_clauses.append(and_(column >= slot_start, column <= slot_end))
            return or_(*time_slot_clauses)
        else:
            return True

    def get_result(self):
        return {
            "number": self.number,
            "name": self.name,
            "from_station_code": self.from_station_code,
            "from_station_name": self.from_station_name,
            "to_station_code": self.to_station_code,
            "to_station_name": self.to_station_name,
            "departure": self.departure,
            "arrival": self.arrival,
            "duration_h": self.duration_h,
            "duration_m": self.duration_m
        }
    
    def decrement_tickets(self, ticket_class):
        column = Train._ticket_class_columns[ticket_class]
        self.__dict__[column.key] = self.__dict__[column.key] - 1

    def __repr__(self):
        return f"<Train {self.number}>"  
