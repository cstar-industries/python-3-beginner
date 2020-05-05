class PocketCalculator:
    """Emulates a simple pocket calculator. PocketCalculator performs basic
    arithmetic on a stored value, and can be reset to 0."""

    def __init__(self):
        """Initializes the PocketCalculator with an internal value set to 0."""
        self.reset()

    def set(self, val: int):
        """Sets the internal value to `val`."""
        self.value = val

    def reset(self):
        """Sets the internal to 0."""
        self.set(0)

    def add(self, val: int):
        """Adds `val` to the internal value."""
        self.value += val

    def sub(self, val: int):
        """Subtracts `val` from the internal value."""
        self.value -= val

    def mul(self, val: int):
        """Multiplies the internal value by `val`."""
        self.value *= val

    def div(self, val: int):
        """Performs integer division on the internal value by `val`."""
        self.value //= val
