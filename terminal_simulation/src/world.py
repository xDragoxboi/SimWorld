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
        self.carrying_capacity = {
            "Human": 10,
            "Herbivore": 20,
            "Carnivore": 5,
            "Plant": 40
        }

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

    def get_lifeforms_of_species(self, species):
        """
        Returns a list of all life forms of the specified species.

        Args:
            species (str): The species to search for.

        Returns:
            list: A list of all life forms of the specified species.
        """
        life_forms = []
        for y in range(self.height):
            for x in range(self.width):
                for entity in self.grid[y][x]:
                    if hasattr(entity, "species") and entity.species == species:
                        life_forms.append(entity)
        return life_forms
