from piccolo.table import Table
from piccolo import columns
from piccolo.columns.column_types import Integer, Text


class Ship(Table):
    """
    Ship Information
    """

    imo_number: Integer = columns.Numeric(primary_key=True)
    name: Text = columns.Text(null=False, unique=True, index=True)
