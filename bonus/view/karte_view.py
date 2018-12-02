from flask import Blueprint, jsonify, request
from controller.karte_controller import get_ticket, update_ticket

karte = Blueprint('karte_view', __name__, url_prefix='/karte')


@karte.route('/<string:uuid>', methods=['GET', 'PATCH'])
def karte_view(uuid):
    if request.method == 'GET':
        ticket = get_ticket(uuid)
        return jsonify(ticket.to_dict()), 200
    if request.method == 'PATCH':
        new_ticket = update_ticket(uuid, request.json)
        return jsonify(new_ticket), 200

