from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine


DB = PostgresEngine(
    config={
        "database": "test_polestar_db",
        "user": "test",
        "password": "P@ssw0rd",
        "host": "localhost",
        "port": 5432,
    }
)


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=["polestar.piccolo_app"])
