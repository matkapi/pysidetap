"""Module processor.py implements the Decision table processor."""


try:
    import pysidetap.libs.operations as operations
except ModuleNotFoundError:
    import libs.operations as operations


class DTProcessor:
    """DTProcessor Decision table processor class."""

    _d_table: list[dict]
    _op: dict = {
        '==': operations.op_eq,
        '!=': operations.op_noteq,
        '>': operations.op_gt,
        '>=': operations.op_gteq,
        '<': operations.op_lt,
        '<=': operations.op_lteq,
        }

    def __init__(self, table: list[dict] = None) -> None:
        if table:
            self.load_table(table)

    def load_table(self, table: list[dict]) -> None:
        """load_table Load decision table into processor.

        Args
        ----
            table: list[dict], optional
                table of fields (operation and values) and return.

        Example
        -------
            Decision Table:
            [
                {
                    'fields': {
                        'field1': {'op':'==','value':1},
                    },
                    'return': 'field1==1'
                },
                {
                    'fields': {
                        'field1': {'op':'!=','value':1},
                    },
                    'return': 'field1!=1'
                }
            ]
        """
        self._d_table = table

    def process(self, values: dict) -> any:
        """Process decision table over values.

        This function find and return field 'return' from Decision Table,
        when all operands in row by 'fields' are True.

        Args
        ----
            values : dict
                Dict of fields that will be evaluated
        
        Example
        -------
            {'field1': 2}

        Returns
        -------
            any
                return value from decision table evaluated row
        """
        for table_row in self._d_table:
            all_pass = True
            if table_row.get('fields'):
                # if decision table row have fields let's evaluate them
                for table_field_key, table_field in table_row['fields'].items():
                    # for each field evaluate operation.
                    # on left side is value on right side is table value
                    res = self._op[table_field['op']](
                        values[table_field_key],
                        table_field['value']
                        )
                    if not res:
                        all_pass &= False
            if all_pass:
                return table_row['return']
        return None
