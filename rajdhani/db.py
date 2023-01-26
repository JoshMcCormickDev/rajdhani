"""
Module to interact with the database.
"""

from . import placeholders
from . import db_ops
db_ops.ensure_db()

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

def search_stations(q):
    """Returns the top ten stations matching the given query string.

    This is used to get show the auto complete on the home page.

    The q is the few characters of the station name or
    code entered by the user.
    """
    # TODO: make a db query to get the matching stations
    # and replace the following dummy implementation
    return placeholders.AUTOCOMPLETE_STATIONS

def get_schedule(train_number):
    """Returns the schedule of a train.
    """
    return placeholders.SCHEDULE

def book_ticket(train_number, ticket_class, departure_date, passenger_name, passenger_email):
    """Book a ticket for passenger
    """
    # TODO: make a db query and insert a new booking
    # into the booking table

    return placeholders.TRIPS[0]

def get_trips(email):
    """Returns the bookings made by the user
    """
    # TODO: make a db query and get the bookings
    # made by user with `email`

    return placeholders.TRIPS
