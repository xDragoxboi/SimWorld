import json
import matplotlib.pyplot as plt

def plot_simulation_data():
    """
    Generates a plot of the simulation data.
    """
    with open("simulation_data.json", "r") as f:
        data = json.load(f)

    steps = sorted([int(step) for step in data.keys()])
    species_data = {}

    for step in steps:
        step_str = str(step)
        for species, values in data[step_str]["life_forms"].items():
            if species not in species_data:
                species_data[species] = {
                    "steps": [],
                    "count": [],
                    "health": [],
                    "energy": [],
                    "size": [],
                }
            species_data[species]["steps"].append(step)
            species_data[species]["count"].append(values["count"])
            species_data[species]["health"].append(values["health"] / values["count"])
            species_data[species]["energy"].append(values["energy"] / values["count"])
            species_data[species]["size"].append(values["size"] / values["count"])

    fig, axs = plt.subplots(4, 1, figsize=(10, 20))

    for species, values in species_data.items():
        axs[0].plot(values["steps"], values["count"], label=species)
    axs[0].set_ylabel("Population")
    axs[0].legend()

    for species, values in species_data.items():
        axs[1].plot(values["steps"], values["health"], label=species)
    axs[1].set_ylabel("Average Health")
    axs[1].legend()

    for species, values in species_data.items():
        axs[2].plot(values["steps"], values["energy"], label=species)
    axs[2].set_ylabel("Average Energy")
    axs[2].legend()

    for species, values in species_data.items():
        axs[3].plot(values["steps"], values["size"], label=species)
    axs[3].set_ylabel("Average Size")
    axs[3].set_xlabel("Step")
    axs[3].legend()

    plt.savefig("simulation_plot.png")
