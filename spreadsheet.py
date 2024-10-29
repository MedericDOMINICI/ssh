
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str):
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
                try:
                    return int(value[1:])
                except ValueError:
                    return "#Error"
            return "#Error"

