from peewee import CharField, IntegerField, Model

from db.settings import db


class User(Model):
    username = CharField(unique=True)
    games_played = IntegerField(default=0)
    highest_score = IntegerField(default=0)
    highest_lvl = IntegerField(default=1)

    class Meta:
        database = db
        # table_name = 'user'
