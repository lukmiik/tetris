from .get_base_dir import BASE_DIR
from db.models.user import User
from db.settings import db
from peewee_migrate import Router

MIGRATE_DIR = BASE_DIR / 'db' / 'migrations'
router = Router(db, migrate_dir=MIGRATE_DIR)


def crete_db() -> None:
    '''Migrates the database'''
    User.create_table()
    router.create('tetris')
    router.run('tetris')
    router.run()


def reset_db() -> None:
    '''Resets the database'''
    User.drop_table()
    User.create_table()
    router.run('tetris')
    router.run()


if __name__ == '__main__':
    reset_db()
