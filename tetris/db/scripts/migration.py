import argparse

from .get_base_dir import BASE_DIR
from db.models.user import User
from db.settings import db
from peewee_migrate import Router

MIGRATE_DIR = BASE_DIR / 'db' / 'migrations'
router = Router(db, migrate_dir=MIGRATE_DIR)


def create_db() -> None:
    '''Migrates the database'''
    User.create_table()
    router.create('tetris')


def reset_db() -> None:
    '''Resets the database'''
    User.drop_table()
    User.create_table()
    router.run('tetris')
    router.run()


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('action', choices=['create', 'reset'])
    args = parse.parse_args()

    if args.action == 'create':
        create_db()
    elif args.action == 'reset':
        reset_db()
