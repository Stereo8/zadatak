import sqlite3
import uuid

from model.team import Team
from model.team_member import TeamMember

DB_PATH = '..\\db\\hzs.db'  # can do abs path too!


def connect():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    conn.commit()
    return conn


def get_all_teams():
    conn = connect()  # todo use connection as context manager
    c = conn.cursor()
    query = """SELECT id, name, description, photo_url, team_uuid FROM team"""
    c.execute(query)
    result_set = c.fetchall()

    teams = []

    for t in result_set:
        created_team = Team(id=t[0], name=t[1], description=t[2], photo_url=t[3], team_uuid=t[4])

        member_query = """SELECT id, first_name, last_name, email, phone_number, school, city FROM 
        team_member WHERE team_id=?"""
        c.execute(member_query, (created_team.id,))
        members = c.fetchall()

        for m in members:
            created_member = TeamMember(id=m[0], first_name=m[1], last_name=m[2], email=m[3], phone_number=m[4],
                                        school=m[5], city=m[6], team=created_team)
            created_team.add_member(created_member)

        teams.append(created_team)

    conn.commit()
    c.close()
    conn.close()

    return teams


def get_team(team_uuid):
    conn = connect()  # todo use connection as context manager
    c = conn.cursor()
    query = """SELECT id, name, description, photo_url, team_uuid FROM team WHERE team_uuid=?"""
    c.execute(query, (team_uuid,))
    t = c.fetchone()

    if t is None:
        return None

    created_team = Team(id=t[0], name=t[1], description=t[2], photo_url=t[3], team_uuid=t[4])

    member_query = """SELECT id, first_name, last_name, email, phone_number, school, city FROM 
    team_member WHERE team_id=?"""
    c.execute(member_query, (created_team.id,))
    members = c.fetchall()

    for m in members:
        created_member = TeamMember(id=m[0], first_name=m[1], last_name=m[2], email=m[3], phone_number=m[4], school=m[5], city=m[6], team=created_team)
        created_team.add_member(created_member)

    conn.commit()
    c.close()
    conn.close()

    return created_team


def create_team(data):
    conn = connect()  # todo use connection as context manager
    c = conn.cursor()

    team_query = """INSERT INTO team (name, description, photo_url, team_uuid) VALUES (?,?,?,?)"""
    team_uuid = uuid.uuid4()
    c.execute(team_query, (data['name'], data['description'], data['photo_url'], str(team_uuid)))
    team_id = c.lastrowid
    data['id'] = team_id
    data['team_uuid'] = team_uuid

    if len(data['team_members']) > 4 or len(data['team_members']) < 3:
        raise ValueError

    for m in data['team_members']:
        member_query = """INSERT INTO team_member (first_name, last_name, email, phone_number, school, city, team_id) 
        VALUES (?,?,?,?,?,?,?)"""
        c.execute(member_query,
                  (m['first_name'], m['last_name'], m['email'], m['phone_number'], m['school'], m['city'], team_id))
        m['id'] = c.lastrowid

    conn.commit()
    c.close()
    conn.close()
    return data


def update_team(data, uuid):
    conn = connect()  # todo use connection as context manager
    c = conn.cursor()

    delete_all_team_members(uuid)

    team_query = """UPDATE team SET name=?, description=?, photo_url=? WHERE team_uuid=?"""

    c.execute(team_query, (data['name'], data['description'], data['photo_url'], uuid))

    if 'team_members' in data:
        for m in data['team_members']:
            member_query = """INSERT INTO team_member (first_name, last_name, email, phone_number, school, city, team_id) 
            VALUES (?,?,?,?,?,?,?)"""
            c.execute(member_query,
                      (m['first_name'], m['last_name'], m['email'], m['phone_number'], m['school'], m['city'], data['id']))
            m['id'] = c.lastrowid

    conn.commit()
    c.close()
    conn.close()
    return data


def delete_team(team_uuid):
    conn = connect()

    with conn:
        team_query = """DELETE FROM team WHERE team_uuid=?"""
        status = conn.execute(team_query, (team_uuid,))
        success = False
        if status.rowcount == 1:
            success = True

    return success


def delete_all_team_members(team_uuid):
    conn = connect()
    try:
        with conn:
            team_query = """DELETE FROM team_member WHERE team_uuid=?"""
            status = conn.execute(team_query, (team_uuid,))
            success = False
            if status.rowcount > 0:
                success = True

            return success
    except sqlite3.Error:
        return False
