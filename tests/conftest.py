import datetime
from piccolo.testing import ModelBuilder
import pytest

from core.db.models.ship import Ship
from core.db.models.ship_position import ShipPositionHistory


@pytest.fixture()
def create_ship():
    ModelBuilder.build_sync(
        Ship,
        defaults={"name": "Mathilde Maersk", "imo_number": "9632179"},
    )


@pytest.fixture(autouse=True)
def clean_db():
    Ship.delete(force=True).run_sync()
    ShipPositionHistory.delete(force=True).run_sync()


@pytest.fixture
def create_ship_positions():
    ship = ModelBuilder.build_sync(
        Ship,
        defaults={"name": "Mathilde Maersk", "imo_number": "9632179"},
    )
    ModelBuilder.build_sync(
        ShipPositionHistory,
        defaults={
            "ship": ship,
            "reported_at": datetime.datetime.strptime(
                "2019-01-14 19:05:32+00", "%Y-%m-%d %H:%M:%S+00"
            ),
            "latitude": "18.4211502075195",
            "longitude": "-64.6109008789062",
        },
    )
    ModelBuilder.build_sync(
        ShipPositionHistory,
        defaults={
            "ship": ship,
            "reported_at": datetime.datetime.strptime(
                "2020-01-14 19:05:32+00", "%Y-%m-%d %H:%M:%S+00"
            ),
            "latitude": "19.4211502075195",
            "longitude": "-65.6109008789062",
        },
    )

    ModelBuilder.build_sync(
        ShipPositionHistory,
        defaults={
            "ship": ship,
            "reported_at": datetime.datetime.strptime(
                "2021-01-14 19:05:32+00", "%Y-%m-%d %H:%M:%S+00"
            ),
            "latitude": "20.4211502075195",
            "longitude": "-66.6109008789062",
        },
    )
