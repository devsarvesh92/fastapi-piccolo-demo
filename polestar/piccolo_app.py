"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

import os

from piccolo.conf.apps import AppConfig

from core.db.models.ship import Ship
from core.db.models.ship_position import ShipPositionHistory


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="polestar",
    migrations_folder_path=os.path.join(CURRENT_DIRECTORY, "piccolo_migrations"),
    table_classes=[Ship, ShipPositionHistory],
    migration_dependencies=[],
    commands=[],
)
