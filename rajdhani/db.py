"""
Module to interact with the database.
"""

from . import placeholders
from . import db_ops
db_ops.ensure_db()

from rajdhani.models.booking import Booking
from rajdhani.models.schedule import Schedule
from rajdhani.models.station import Station
from rajdhani.models.train import Train

def search_trains(
        from_station_code,
        to_station_code,
        ticket_class=None,
        departure_date=None,
        departure_time=[],
        arrival_time=[]):
    """Returns all the trains that source to destination stations on
    the given date. When ticket_class is provided, this should return
    only the trains that have that ticket class.

    This is used to get show the trains on the search results page.
    """
    with db_ops.Session() as session:
        q = (
            session
            .query(Train)
            .where(Train.from_station_code == from_station_code)
            .where(Train.to_station_code == to_station_code)
            .where(Train.is_ticket_class(ticket_class))
            .where(Train.is_in_time_slots(departure_time, arrival_time))
        )
        return [row.get_result() for row in q.all()]


def search_stations(search):
    """Returns the top ten stations matching the given query string.

    This is used to get show the auto complete on the home page.

    The q is the few characters of the station name or
    code entered by the user.
    """
    with db_ops.Session() as session:
        q = (
            session
            .query(Station)
            .where(Station.matches_search(search))
        )
        return [row.get_result() for row in q.all()]


def get_schedule(train_number):
    """Returns the schedule of a train.
    """
    with db_ops.Session() as session:
        q = (
            session
            .query(Schedule)
            .where(Schedule.train_number == train_number)
        )
        return [row.get_result() for row in q.all()]


def book_ticket(train_number, ticket_class, departure_date, passenger_name, passenger_email):
    """Book a ticket for passenger
    """
    with db_ops.Session() as session:
        train_q = (
            session
            .query(Train)
            .where(Train.number == train_number)
        )

        train = train_q.one()

        booking = Booking()
        booking.train_number = train_number
        booking.from_station_code = train.from_station_code
        booking.to_station_code = train.to_station_code
        booking.passenger_name = passenger_name
        booking.passenger_email = passenger_email
        booking.ticket_class = ticket_class
        booking.date = departure_date
        session.add(booking)
        session.commit()

        return booking.get_result()


def get_trips(email):
    """Returns the bookings made by the user
    """
    # TODO: make a db query and get the bookings
    # made by user with `email`

    return placeholders.TRIPS
