from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Numeric
from piccolo.columns.column_types import Text
from piccolo.columns.column_types import Timestamptz
from piccolo.columns.defaults.timestamptz import TimestamptzNow
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table
import decimal


class Ship(Table, tablename="ship", schema=None):
    imo_number = Numeric(
        default=decimal.Decimal("0"),
        digits=None,
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


ID = "2023-11-20T20:12:13:215023"
VERSION = "1.1.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="polestar", description=DESCRIPTION
    )

    manager.add_table(
        class_name="ShipPositionHistory",
        tablename="ship_position_history",
        schema=None,
        columns=None,
    )

    manager.add_table(class_name="Ship", tablename="ship", schema=None, columns=None)

    manager.add_column(
        table_class_name="ShipPositionHistory",
        tablename="ship_position_history",
        column_name="imo_number",
        db_column_name="imo_number",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": Ship,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="ShipPositionHistory",
        tablename="ship_position_history",
        column_name="reported_at",
        db_column_name="reported_at",
        column_class_name="Timestamptz",
        column_class=Timestamptz,
        params={
            "default": TimestamptzNow(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": True,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="ShipPositionHistory",
        tablename="ship_position_history",
        column_name="latitude",
        db_column_name="latitude",
        column_class_name="Numeric",
        column_class=Numeric,
        params={
            "default": decimal.Decimal("0"),
            "digits": (16, 13),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="ShipPositionHistory",
        tablename="ship_position_history",
        column_name="longitude",
        db_column_name="longitude",
        column_class_name="Numeric",
        column_class=Numeric,
        params={
            "default": decimal.Decimal("0"),
            "digits": (16, 13),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Ship",
        tablename="ship",
        column_name="imo_number",
        db_column_name="imo_number",
        column_class_name="Numeric",
        column_class=Numeric,
        params={
            "default": decimal.Decimal("0"),
            "digits": None,
            "null": False,
            "primary_key": True,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Ship",
        tablename="ship",
        column_name="name",
        db_column_name="name",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": True,
            "index": True,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    return manager
