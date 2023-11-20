from piccolo.table import Table
from piccolo import columns
from piccolo.columns.column_types import Integer, Text, Timestamptz, Numeric

from core.db.models.ship import Ship


class ShipPositionHistory(Table):
    """Represents ship position history"""

    imo_number = columns.ForeignKey(references=Ship)
    reported_at: Timestamptz = columns.Timestamptz(null=False, index=True)
    latitude: Numeric = columns.Numeric(
        digits=(16, 13),
        null=False,
    )
    longitude: Numeric = columns.Numeric(
        digits=(16, 13),
        null=False,
    )
