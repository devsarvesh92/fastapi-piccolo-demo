from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

from settings import ENVSETTINGS


DB = PostgresEngine(
    config={
        "database": ENVSETTINGS.database_name,
        "user": ENVSETTINGS.database_user,
        "password": ENVSETTINGS.database_password,
        "host": ENVSETTINGS.database_host,
        "port": ENVSETTINGS.database_port,
    }
)


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=["polestar.piccolo_app"])
