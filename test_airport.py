import pytest
from passengers_class import *
from planes_class import *
from flight_trip_class import *

def test_passenger():
    assert Passengers('Joana Thompson', 'B343123').name == 'Joana Thompson'
    assert Passengers('Birt Kuman', 'B13927').passport_number == 'B13927'


def test_planes():
    assert Planes('1234').plane_number == '1234'
    assert Planes('5678').plane_number == '5678'

def test_flight_trip_init():
    new_trip = Flight_trip()
    #ASSERTION
    # check that no errors occurred or check if data type is of specific class
    assert isinstance(new_trip, Flight_trip) == True

def test_flight_trip_add_destination():
    new_trip = Flight_trip()
    new_trip.add_destination('LA')
    assert new_trip.destination == 'LA'

def test_flight_trip_add_origin():
    new_trip = Flight_trip()
    new_trip.add_origin('London')
    assert new_trip.origin == 'London'

def test_flight_trip_add_plane():
    new_trip = Flight_trip()
    new_trip.add_plane('BA707')
    assert new_trip.plane == 'BA707'

def test_flight_trip_add_passenger():
    new_trip = Flight_trip()
    new_trip.add_passenger('Joana Thompson')
    assert new_trip.passengers[0] == 'Joana Thompson'
    assert type(new_trip.passengers) == type([])