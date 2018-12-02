import json

from flask import Blueprint, request, jsonify

from controller.main_controller import get_all_teams, create_team, get_team, update_team, delete_team
from controller.member_controller import get_member, update_member, delete_member
teams = Blueprint('teams', __name__, url_prefix='/teams')
members = Blueprint('members', __name__, url_prefix='/members')


@teams.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@teams.route('/', methods=['GET', 'POST'])
def teams_view():
    if request.method == 'GET':  # get all teams
        all_teams = get_all_teams()

        response_body = [t.to_dict() for t in all_teams]
        return jsonify(response_body), 200

    if request.method == 'POST':  # create a new team
        # mention validation issues
        body = request.json
        try:
            created = create_team(body)
        except ValueError:
            return 'Broj clanova mora biti 3 ili 4', 400
        return jsonify(created), 201


@teams.route('/<string:team_uuid>', methods=['GET', 'PUT', 'DELETE'])
def single_team_view(team_uuid):
    if request.method == 'GET':  # get the team
        team = get_team(team_uuid)
        if team is None:
            return jsonify({'error': 'team with unique id {} not found'.format(team_uuid)}), 404

        response_body = team.to_dict()
        return jsonify(response_body), 200

    if request.method == 'PUT':  # update the team
        body = request.json
        updated = update_team(body, team_uuid)
        if updated is None:
            return jsonify({'error': 'team with unique id {} not found'.format(team_uuid)}), 404

        return jsonify(updated), 200

    if request.method == 'DELETE':  # remove the team
        success = delete_team(team_uuid)

        if not success:
            return jsonify({'error': 'team with unique id {} not found'.format(team_uuid)}), 404

        return jsonify({}), 204


@members.route('/<int:member_id>', methods=['GET', 'PUT', 'DELETE'])
def member_view(member_id):
    if request.method == 'GET':
        try:
            member = get_member(member_id)
        except FileNotFoundError:
            return 'Member sa ovim id-jem nije pronadjen', 404

        return jsonify(member.to_dict()), 200

    if request.method == 'PUT':
        json = request.json
        member = update_member(member_id, json)
        if member is None:
            return 'Member sa ovim id-jem nije pronadjen', 404
        return jsonify(member.to_dict()), 200

    if request.method == 'DELETE':
        status = delete_member(member_id)
        if status == 404:
            return 'Member sa ovim id-jem nije pronadjen', 404
        if status == 400:
            return 'Ne sme biti manje od 3 clana u timu', 400
        if status == 204:
            return jsonify({}), 204




