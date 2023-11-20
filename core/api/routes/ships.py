"""Ship module"""

from http import HTTPStatus
from typing import Any
from core.api.application import app
from core.api.constants import Constants
from core.api.schema.responses import ShipInformation
from core.db.models.ship import Ship


@app.get(
    path=Constants.SHIPS,
    status_code=HTTPStatus.OK,
    description="Get all ships from polestar",
    tags=["polestar"],
    summary="Get all ships from polestar",
    operation_id="get_ships",
    response_model=list[ShipInformation],
)
async def get_ships() -> list[ShipInformation]:
    """
    Get all ships

    Returns: Details of all ships
    rtype: list[ShipInformation]
    """
    ships: list[dict[str, Any]] = await Ship.select(Ship.name, Ship.imo_number)

    return [
        ShipInformation(name=ship["name"], imo_number=ship["imo_number"])
        for ship in ships
    ]


@app.post(
    path=Constants.SHIPS,
    status_code=HTTPStatus.CREATED,
    description="Create ship for polestar",
    tags=["polestar"],
    summary="Create ship for polestar",
    operation_id="create ship",
)
async def create_ship(ship_info: ShipInformation) -> None:
    """
    Create ship

    Returns: None
    rtype: None
    """
    await Ship.insert(
        Ship(name=ship_info.name, imo_number=ship_info.imo_number)
    ).on_conflict(action="DO NOTHING")
