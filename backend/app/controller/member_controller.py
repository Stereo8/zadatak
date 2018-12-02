import sqlite3
from controller.main_controller import connect
from model.team_member import TeamMember
from model.team import Team


def get_member(member_id):
    conn = connect()
    c = conn.cursor()
    query = """SELECT id, first_name, last_name, email, phone_number, school, city, team_id FROM 
    team_member WHERE id=?"""
    c.execute(query, (member_id,))
    member_row = c.fetchone()

    if member_row is None:
        raise FileNotFoundError

    c.execute("""SELECT id, name, description, photo_url, team_uuid FROM team WHERE id=?""", (member_row[7],))
    team_row = c.fetchone()

    team = Team(id=team_row[0], name=team_row[1], description=team_row[2], photo_url=team_row[3], team_uuid=team_row[4])

    created_member = TeamMember(id=member_row[0], first_name=member_row[1], last_name=member_row[2], email=member_row[3], phone_number=member_row[4], school=member_row[5], city = member_row[6], team=team)

    conn.commit()
    c.close()
    conn.close()
    return created_member

def update_member(member_id, data):
    conn = connect()
    c = conn.cursor()
    query = """SELECT id, first_name, last_name, email, phone_number, school, city, team_id FROM 
        team_member WHERE id=?"""
    c.execute(query, (member_id,))

    update_query = """UPDATE team_member SET first_name=?, last_name=?, email=?, phone_number=?, school=?, city=? WHERE id=?"""

    c.execute(update_query, (data['first_name'], data['last_name'], data['email'], data['phone_number'], data['school'], data['city'], member_id))

    c.execute(query, (member_id,))
    member_row = c.fetchone()

    c.execute("""SELECT id, name, description, photo_url, team_uuid FROM team WHERE id=?""", (member_row[7],))
    team_row = c.fetchone()
    team = Team(id=team_row[0], name=team_row[1], description=team_row[2], photo_url=team_row[3], team_uuid=team_row[4])

    updated_member = TeamMember(id=member_row[0], first_name=member_row[1], last_name=member_row[2], email=member_row[3], phone_number=member_row[4], school=member_row[5], city = member_row[6], team=team)

    conn.commit()
    c.close()
    conn.close()
    return updated_member

def delete_member(member_id):
    conn = connect()
    c = conn.cursor()
    query = """SELECT id, first_name, last_name, email, phone_number, school, city, team_id FROM 
            team_member WHERE id=?"""
    c.execute(query, (member_id,))
    member_row = c.fetchone()
    if member_row is None:
        return 404

    select_query = """SELECT id, first_name, last_name, email, phone_number, school, city, team_id FROM 
            team_member WHERE team_id=?"""

    c.execute(select_query, (member_row[7],))
    team_members = c.fetchall()
    if len(team_members) <= 3:
        return 400

    delete_query = """DELETE FROM team_member WHERE id=?"""

    conn.execute(delete_query, (member_id,))

    conn.commit()
    c.close()
    conn.close()

    return 204






