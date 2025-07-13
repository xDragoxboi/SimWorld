from terminal_simulation.src.simulation import Simulation
from terminal_simulation.src.plotting import plot_simulation_data

def main():
    """
    The main function of the program.
    """
    simulation = Simulation(20, 10)
    simulation.run(600)
    plot_simulation_data()

if __name__ == "__main__":
    main()
