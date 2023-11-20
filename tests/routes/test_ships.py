from http import HTTPStatus
import pytest
from httpx import AsyncClient
from core.api.constants import Constants
from core.api.routes.ships import app
from core.api.schema.responses import ShipInformation
from core.db.models.ship import Ship


pytestmark = pytest.mark.ships


@pytest.mark.asyncio()
async def test_returns_ships(clean_db, create_ship):
    async with AsyncClient(
        app=app, follow_redirects=True, base_url="http://localhost:8000"
    ) as client:
        resp = await client.get(
            Constants.SHIPS,
            headers={},
            params={},
        )
        data = resp.json()
        assert len(data) == 1

        ship_info = data[0]
        assert ship_info["name"] == "Mathilde Maersk"
        assert ship_info["imo_number"] == 9632179

        assert resp.status_code == HTTPStatus.OK


@pytest.mark.asyncio()
async def test_creates_ship(clean_db, create_ship):
    async with AsyncClient(
        app=app, follow_redirects=True, base_url="http://localhost:8000"
    ) as client:
        resp = await client.post(
            Constants.SHIPS,
            headers={},
            data=ShipInformation(name="XYZ", imo_number=12345).model_dump_json(),
            params={},
        )
        assert resp.status_code == HTTPStatus.CREATED
        fetched_ship = Ship.objects().get(Ship.imo_number == 12345).run_sync()
        assert fetched_ship.name == "XYZ"
