from terminal_simulation.src.item import Item
from terminal_simulation.src.lifeform import LifeForm


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
        Renders the world to the console.
        """
        for y in range(self.world.height):
            for x in range(self.world.width):
                cell = self.world.grid[y][x]
                if not cell:
                    print("  ", end="")
                else:
                    # Prioritize rendering lifeforms over items
                    lifeform_in_cell = next((obj for obj in cell if isinstance(obj, LifeForm)), None)
                    if lifeform_in_cell:
                        print(f" {lifeform_in_cell.name[0]}", end="")
                    else:
                        item_in_cell = next((obj for obj in cell if isinstance(obj, Item)), None)
                        if item_in_cell:
                            print(f" {item_in_cell.name[0]}", end="")
                        else:
                            print("  ", end="")
            print()
