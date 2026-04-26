from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Create a king object."""

    def __init__(self, first_name, is_alive=True):
        """King constructor."""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Get eyes color."""
        return self.eyes

    def get_hairs(self):
        """Get hairs color."""
        return self.hairs

    def set_eyes(self, color):
        """Set eyes color."""
        self.eyes = color

    def set_hairs(self, color):
        """Set hairs color."""
        self.hairs = color
