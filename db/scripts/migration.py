import argparse

from get_base_dir import BASE_DIR
from peewee_migrate import Router

from db.models.user import User
from db.settings import db

MIGRATE_DIR = BASE_DIR / 'db' / 'migrations'
router = Router(db, migrate_dir=MIGRATE_DIR)


def create_user_table() -> None:
    '''Create the user table'''
    User.create_table()


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('action', choices=['create', 'migrate', 'rollback'])
    parse.add_argument('-n', '--name')
    parse.add_argument('-optional_arg')
    args = parse.parse_args()

    if args.action == 'create':
        router.create(args.name) if args.name else router.create()
    elif args.action == 'migrate':
        router.run(args.name) if args.name else router.run()
        create_user_table()
    elif args.action == 'rollback':
        router.rollback()
