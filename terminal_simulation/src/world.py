import random

class World:
    """
    The World class manages the simulation's environment, including the grid, biomes, and weather.
    """

    def __init__(self, width, height):
        """
        Initializes a new World object.

        Args:
            width (int): The width of the world in grid cells.
            height (int): The height of the world in grid cells.
        """
        self.width = width
        self.height = height
        self.grid = [[[] for _ in range(width)] for _ in range(height)]
        self.biomes = [[None for _ in range(width)] for _ in range(height)]
        self.weather = "sunny"

    def generate_world(self):
        """
        Generates the world's terrain and biomes.
        """
        for y in range(self.height):
            for x in range(self.width):
                self.biomes[y][x] = self._generate_biome()

    def _generate_biome(self):
        """
        Generates a random biome.

        Returns:
            str: The name of the biome.
        """
        biomes = ["forest", "plains", "desert", "mountains", "ocean"]
        return random.choice(biomes)
