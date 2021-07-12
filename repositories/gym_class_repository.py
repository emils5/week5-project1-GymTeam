from db.run_sql import run_sql

from models.gym_class import Gym_class
from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_classes( name ) VALUES ( %s ) RETURNING id"
    values = [gym_class.name]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    gym_classes = []

    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    for row in results:
        gym_class = Gym_class(row['name'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)