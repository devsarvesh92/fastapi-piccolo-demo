from piccolo.apps.migrations.auto.migration_manager import MigrationManager


ID = "2023-11-20T23:42:43:697470"
VERSION = "1.1.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="polestar", description=DESCRIPTION
    )

    manager.rename_column(
        table_class_name="ShipPositionHistory",
        tablename="ship_position_history",
        old_column_name="imo_number",
        new_column_name="ship",
        old_db_column_name="imo_number",
        new_db_column_name="ship",
        schema=None,
    )

    return manager
