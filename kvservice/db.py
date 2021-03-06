from .kv_store import KVStore
from flask import current_app, g
import click
from flask.cli  import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = KVStore(current_app.config['DATABASE'])
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.conn.executescript(f.read().decode('utf8'))

  

def init_app(app):
    app.teardown_appcontext(close_db)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')