from piccolo.testing import ModelBuilder
import pytest

from core.db.models.ship import Ship


@pytest.fixture()
def create_ship():
    ModelBuilder.build_sync(
        Ship,
        defaults={"name": "Mathilde Maersk", "imo_number": "9632179"},
    )


@pytest.fixture(autouse=True)
def clean_db():
    Ship.delete(force=True).run_sync()
