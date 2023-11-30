from peewee import SqliteDatabase

DB_NAME = 'db.sqlite3'
pragmas = {'journal_mode': 'wal', 'cache_size': -1024 * 4, 'foreign_keys': 1}

db = SqliteDatabase(DB_NAME, pragmas=pragmas)
