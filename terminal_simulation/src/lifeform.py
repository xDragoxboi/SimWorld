import random

class LifeForm:
    """
    The LifeForm class is the base class for all organisms in the simulation.
    """

    def __init__(self, name, species, health, energy, size, dna=None):
        """
        Initializes a new LifeForm object.

        Args:
            name (str): The name of the life form.
            species (str): The species of the life form.
            health (int): The health of the life form.
            energy (int): The energy of the life form.
            size (int): The size of the life form in kilograms.
            dna (list, optional): The DNA of the life form. Defaults to None.
        """
        self.name = name
        self.species = species
        self.health = health
        self.energy = energy
        self.size = size
        self.x = 0
        self.y = 0
        if dna is None:
            self.dna = [random.random() for _ in range(10)]
        else:
            self.dna = dna

    def move(self, dx, dy):
        """
        Moves the life form by the specified amount.

        Args:
            dx (int): The change in the x-coordinate.
            dy (int): The change in the y-coordinate.
        """
        self.x += dx
        self.y += dy

    def eat(self, food):
        """
        Eats the specified food.

        Args:
            food (LifeForm): The food to eat.
        """
        if self.species == "Herbivore" and food.species == "Plant":
            self.energy += food.energy
            food.health = 0
        elif self.species == "Human" and food.species == "Herbivore":
            self.energy += food.energy
            food.health = 0

    def reproduce(self, other):
        """
        Reproduces a new life form with another life form.

        Args:
            other (LifeForm): The other life form to reproduce with.

        Returns:
            LifeForm: The new life form.
        """
        new_dna = []
        for i in range(len(self.dna)):
            if random.random() < 0.5:
                new_dna.append(self.dna[i])
            else:
                new_dna.append(other.dna[i])

        for i in range(len(new_dna)):
            if random.random() < 0.1:  # 10% chance of mutation
                new_dna[i] += (random.random() - 0.5) * 0.1  # Small random change

        new_species = self.species
        if self.species != other.species:
            new_species = f"{self.species}-{other.species}"

        return LifeForm(
            self.name,
            new_species,
            (self.health + other.health) / 2,
            (self.energy + other.energy) / 2,
            (self.size + other.size) / 2,
            new_dna,
        )
