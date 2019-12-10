import pytest
from passengers_class import *
from planes_class import *
from flight_trip_class import *

def test_passenger():
    passenger1 = Passengers('Joana Thompson', 'B343123')
    passenger2 = Passengers('Birt Kuman', 'B13927')
    assert passenger1.name == 'Joana Thompson'
    assert passenger2.passport_number == 'B13927'

def test_missing_info():
    with pytest.raises(TypeError):
        Passengers()
    with pytest.raises(TypeError):
        Passengers('Joana Thompson')
    with pytest.raises(TypeError):
        Passengers('B343123')


def test_planes():
    new_plane = Planes('8901')
    # assert Planes('1234').plane_number == '1234'
    # assert Planes('5678').plane_number == '5678'
    assert isinstance(new_plane, Planes)

def test_flight_trip_init():
    new_trip = Flight_trip()
    #ASSERTION
    # check that no errors occurred or check if data type is of specific class
    assert isinstance(new_trip, Flight_trip)

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