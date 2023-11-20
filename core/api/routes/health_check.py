from http import HTTPStatus
from core.api.application import app
from core.api.constants import Constants


@app.get(
    path=Constants.HEALTH_CHECK_URI,
    status_code=HTTPStatus.OK,
    description="Health check status of polestar service",
    tags=["polestar"],
    summary="Get health check status",
    operation_id="get_ht",
    response_model=dict[str, str],
)
async def ht():
    """
    Health check

    Returns: Empty response
    rtype: dict[str,str]
    """
    return {}
