
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self.get(cell)
        if value.isdigit():
            return int(value)
        try:
            float(value)  # Check if it can be converted to a float
            return "#Error"
        except ValueError:
            if value.startswith("'") and value.endswith("'"):
                return value[1:-1]
            elif value.startswith("='") and value.endswith("'"):
                return value[2:-1]
            elif value.startswith("="):
                if value[1:].isdigit():
                    return int(value[1:])
                else:
                    # Assume the rest is a cell reference
                    referenced_value = self.get(value[1:])
                    if referenced_value.isdigit():
                        return int(referenced_value)
                    else:
                        return "#Error"
            return "#Error"

