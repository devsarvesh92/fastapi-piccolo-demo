import datetime
import uuid
from pydantic import BaseModel as PydanticBaseModel, Extra


class BaseModel(PydanticBaseModel):
    """Defines pydantic base model with custom config."""

    class Config:
        """Defines custom pydantic config for base model."""

        anystr_strip_whitespace = True
        arbitrary_types_allowed = True
        extras = Extra.forbid
        json_encoders = {
            datetime.datetime: lambda val: val.strftime(
                Constants.EVENT_TIMESTAMP_FORMAT
            ),
            uuid.UUID: str,
        }


class ShipInformation(BaseModel):
    """
    Defines ship information model
    """

    name: str
    imo_number: int
