from peewee import CharField, IntegerField
from playhouse.signals import Model, pre_save

from db.settings import db


class User(Model):
    '''Model for user table'''

    username = CharField(unique=True)
    games_played = IntegerField(default=0)
    highest_score = IntegerField(default=0)
    lvl = IntegerField(default=1)

    class Meta:
        database = db


def user_exists(username) -> bool:
    '''Checks if a user exists in the database'''
    return User.select().where(User.username == username).exists()


@pre_save(sender=User)
def on_save_handler(model_class, instance, created) -> None:
    '''Increments games_played field on save'''
    instance.games_played += 1
