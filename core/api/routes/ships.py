"""Ship module"""

import datetime
from http import HTTPStatus
from typing import Any

from fastapi import HTTPException
from core.api.application import app
from core.api.constants import Constants
from core.api.schema.responses import ShipInformation, ShipPosition
from core.db.models.ship import Ship
from core.db.models.ship_position import ShipPositionHistory


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


@app.get(
    path=Constants.SHIP_POSITIONS,
    status_code=HTTPStatus.OK,
    description="Get all positions sorted by latest timestamp",
    tags=["polestar"],
    summary="Get all positions sorted by latest timestamp",
    operation_id="get positions",
)
async def get_ship_positions(imo: int) -> list[ShipPosition]:
    """Get ship positions by imo

    Args:
        imo (int): Imo number

    Raises:
        HTTPException: 404

    Returns:
        list[ShipPosition]: Ship positions sorted by latest timestamp
    """
    ship_positions: list[ShipPositionHistory] = (
        ShipPositionHistory.select(
            ShipPositionHistory.ship.name,
            ShipPositionHistory.ship.imo_number,
            ShipPositionHistory.latitude,
            ShipPositionHistory.longitude,
            ShipPositionHistory.reported_at,
        )
        .where(ShipPositionHistory.ship.imo_number == imo)
        .order_by(ShipPositionHistory.reported_at, ascending=False)
        .run_sync()
    )

    if not ship_positions:
        raise HTTPException(
            status_code=404, detail=f"Ship positions for {imo=} not found"
        )

    return [
        ShipPosition(
            imo_number=sp["ship.imo_number"],
            name=sp["ship.name"],
            latitude=sp["latitude"],
            longitude=sp["longitude"],
            reported_at=sp["reported_at"],
        )
        for sp in ship_positions
    ]
