from flask import Blueprint, jsonify, request
from controller.letovi_controller import get_all_flights, flight_lookup, get_flight,reserve_ticket

letovi = Blueprint('letovi_view', __name__, url_prefix='/letovi')


@letovi.route('/', methods=['GET'])
def all_flights():
    all_flights = get_all_flights()
    response_list = [f.to_dict() for f in all_flights]
    return jsonify(response_list), 200


@letovi.route('/<string:dep>-<string:arr>', methods=['GET'])
def flight_by_airport(dep, arr):
    if request.method == 'GET':
        found_flights = flight_lookup(dep.lower(), arr.lower())
        response_list = [f.to_dict() for f in found_flights]
        return jsonify(response_list), 200


@letovi.route('/<string:broj_leta>', methods=['GET', 'POST'])
def single_flight_view(broj_leta):
    if request.method == 'GET':
        flight = get_flight(broj_leta)
        response = jsonify(flight.to_dict())
        return response, 200
    if request.method == 'POST':
        data = request.json
        response = reserve_ticket(broj_leta, data)
        if response == 400:
            return 'Klasa mora biti economy, business ili first', 400
        if response == 403:
            return 'Nema slobodnih mesta u datoj klasi', 403
        return jsonify(response), 201
