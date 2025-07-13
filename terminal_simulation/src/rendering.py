class Renderer:
    """
    The Renderer class is responsible for displaying the state of the world in the terminal.
    """

    def __init__(self, world):
        """
        Initializes a new Renderer object.

        Args:
            world (World): The world to render.
        """
        self.world = world

    def render(self):
        """
        Renders the world to the terminal.
        """
        for y in range(self.world.height):
            for x in range(self.world.width):
                cell = self.world.grid[y][x]
                if cell is None:
                    print(".", end="")
                else:
                    print(cell.name[0], end="")
            print()
