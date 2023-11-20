"""This module defines a FastAPI application instance."""


from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

######################
# App
######################
app: FastAPI = FastAPI(
    debug=False,
    title="Polestar ship tracking api",
    description="""This service provides results by performing Sync &
     Async Queries to the underlying ship positions.""",
    version="1.0",
    openapi_tags=[
        {
            "name": "polestar",
            "description": """Provides results by performing Sync &
            Async Queries to the underlying ship positions.""",
        }
    ],
)

# Add middlewares
app.add_middleware(CORSMiddleware)
