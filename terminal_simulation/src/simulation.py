import time
from .world import World
from .lifeform import LifeForm
from .blueprint import Blueprint
from .rendering import Renderer

class Simulation:
    """
    The Simulation class is responsible for running the simulation.
    """

    def __init__(self, width, height):
        """
        Initializes a new Simulation object.

        Args:
            width (int): The width of the world in grid cells.
            height (int): The height of the world in grid cells.
        """
        self.world = World(width, height)
        self.life_forms = []
        self.renderer = Renderer(self.world)

    def run(self, steps):
        """
        Runs the simulation for the specified number of steps.

        Args:
            steps (int): The number of steps to run the simulation for.
        """
        self.world.generate_world()
        self._spawn_life_forms()

        for i in range(steps):
            print(f"Step {i + 1}")
            self.renderer.render()
            self._update()
            time.sleep(1)

    def _spawn_life_forms(self):
        """
        Spawns life forms into the world.
        """
        # Spawn humans
        human_blueprint = Blueprint("blueprints/human.xml")
        attributes = human_blueprint.get_attributes()
        for _ in range(5):
            human = LifeForm(
                human_blueprint.get_name(),
                human_blueprint.get_species(),
                attributes["health"],
                attributes["energy"],
                attributes["size"],
            )
            self.life_forms.append(human)
            self.world.grid[random.randint(0, self.world.height - 1)][
                random.randint(0, self.world.width - 1)
            ] = human

        # Spawn herbivores
        herbivore_blueprint = Blueprint("blueprints/herbivore.xml")
        attributes = herbivore_blueprint.get_attributes()
        for _ in range(10):
            herbivore = LifeForm(
                herbivore_blueprint.get_name(),
                herbivore_blueprint.get_species(),
                attributes["health"],
                attributes["energy"],
                attributes["size"],
            )
            self.life_forms.append(herbivore)
            self.world.grid[random.randint(0, self.world.height - 1)][
                random.randint(0, self.world.width - 1)
            ] = herbivore

        # Spawn plants
        plant_blueprint = Blueprint("blueprints/plant.xml")
        attributes = plant_blueprint.get_attributes()
        for _ in range(20):
            plant = LifeForm(
                plant_blueprint.get_name(),
                plant_blueprint.get_species(),
                attributes["health"],
                attributes["energy"],
                attributes["size"],
            )
            self.life_forms.append(plant)
            self.world.grid[random.randint(0, self.world.height - 1)][
                random.randint(0, self.world.width - 1)
            ] = plant

    def _update(self):
        """
        Updates the simulation by one step.
        """
        for life_form in self.life_forms:
            if life_form.health <= 0:
                self.life_forms.remove(life_form)
                self.world.grid[life_form.y][life_form.x] = None
            else:
                # For now, we'll just print the life form's status.
                print(
                    f"  {life_form.name}: "
                    f"Health={life_form.health}, "
                    f"Energy={life_form.energy}, "
                    f"Size={life_form.size}"
                )
