class Item:
    """
    The Item class represents an item in the simulation.
    """

    def __init__(self, name, size):
        """
        Initializes a new Item object.

        Args:
            name (str): The name of the item.
            size (int): The size of the item in kilograms.
        """
        self.name = name
        self.size = size
        self.x = 0
        self.y = 0
