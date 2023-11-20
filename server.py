"""This module defines the web server entry-point."""


from contextlib import asynccontextmanager
import logging
from core.api.application import app
from core.api.routes.health_check import ht
from piccolo_conf import DB
from settings import ENVSETTINGS

LOGGER = logging.getLogger(name=__name__)

LOGGER.info(f" Health check: {ht}")


################################################################################
# Define triggers for startup and shutdown operations!
################################################################################
@asynccontextmanager
async def lifespan() -> None:
    """
    This function is called when the server starts up.

    :return: None
    """
    LOGGER.info("Starting web server...")
    await DB.start_connection_pool(
        min_size=1, max_size=ENVSETTINGS.db_connection_pool_size
    )
    yield
    await DB.close_connection_pool()
