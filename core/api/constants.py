from typing import Final, LiteralString


class Constants:
    # Routes
    HEALTH_CHECK_URI: Final[LiteralString] = "/ht"
    SHIPS: Final[LiteralString] = "/api/ships"
    GET_SHIP_POSITIONS: Final[LiteralString] = "/api/positions/{imo}"
