"""Manages data ingestion"""


import datetime
import logging
from typing import Any
from asyncpg import UniqueViolationError
import pandas as pd
from core.db.models.ship import Ship
from core.db.models.ship_position import ShipPositionHistory

LOGGER = logging.getLogger(__name__)


def ingest_ships():
    """
    Ingest ships
    """
    try:
        Ship.insert(
            Ship(name="Mathilde Maersk", imo_number=9632179),
            Ship(name="Australian Spirit", imo_number=9247455),
            Ship(name="MSC Preziosa", imo_number=9595321),
        ).run_sync()
    except UniqueViolationError:
        LOGGER.error("Ignoring this as ships already exists")


def ingest_ship_position():
    """
    Ingest ship positions
    """

    LOGGER.info("[START] Ship positions ingestion")

    ship_positions = pd.read_csv("./data/positions.csv")
    imo_numbers = [
        int(imo_number) for imo_number in ship_positions["imo_number"].unique()
    ]

    ships = Ship.objects().where(Ship.imo_number.is_in(imo_numbers)).run_sync()
    ship_map = {int(ship.imo_number): ship for ship in ships}

    ship_position_history = []
    for _, row in ship_positions.iterrows():
        ship_position_history.append(
            ShipPositionHistory(
                ship=ship_map[int(row["imo_number"])],
                reported_at=datetime.datetime.strptime(
                    row["reported_at"], "%Y-%m-%d %H:%M:%S+00"
                ),
                latitude=row["latitude"],
                longitude=row["longitude"],
            )
        )
    ShipPositionHistory.insert(*ship_position_history).on_conflict(
        action="DO NOTHING",
    ).run_sync()

    LOGGER.info("[END] Ship positions ingestion")


if __name__ == "__main__":
    ingest_ships()
    ingest_ship_position()
