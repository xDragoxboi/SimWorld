import json
import matplotlib.pyplot as plt

def plot_simulation_data():
    """
    Plots the simulation data from the simulation_data.json file.
    """
    with open("simulation_data.json", "r") as f:
        data = json.load(f)

    steps = sorted([int(step) for step in data.keys()])
    life_form_data = {}
    item_data = {}

    for step in steps:
        step_str = str(step)
        # Life form data
        if "life_forms" in data[step_str]:
            for species, species_data in data[step_str]["life_forms"].items():
                if species not in life_form_data:
                    life_form_data[species] = {"count": [], "health": [], "energy": [], "size": []}
                life_form_data[species]["count"].append(species_data["count"])
                life_form_data[species]["health"].append(species_data["health"] / species_data["count"])
                life_form_data[species]["energy"].append(species_data["energy"] / species_data["count"])
                life_form_data[species]["size"].append(species_data["size"] / species_data["count"])
        # Item data
        if "items" in data[step_str]:
            for item_name, item_name_data in data[step_str]["items"].items():
                if item_name not in item_data:
                    item_data[item_name] = {"count": [], "size": []}
                item_data[item_name]["count"].append(item_name_data["count"])
                if item_name_data["count"] > 0:
                    item_data[item_name]["size"].append(item_name_data["size"] / item_name_data["count"])
                else:
                    item_data[item_name]["size"].append(0)

    # Plotting
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))

    # Life form counts
    for species, species_data in life_form_data.items():
        axs[0, 0].plot(steps, species_data["count"], label=f"{species} Count")
    axs[0, 0].set_xlabel("Step")
    axs[0, 0].set_ylabel("Count")
    axs[0, 0].set_title("Life Form Counts Over Time")
    axs[0, 0].legend()
    axs[0, 0].grid(True)

    # Item counts
    for item_name, item_name_data in item_data.items():
        axs[0, 1].plot(steps, item_name_data["count"], label=f"{item_name} Count")
    axs[0, 1].set_xlabel("Step")
    axs[0, 1].set_ylabel("Count")
    axs[0, 1].set_title("Item Counts Over Time")
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    # Average health
    for species, species_data in life_form_data.items():
        axs[1, 0].plot(steps, species_data["health"], label=f"{species} Avg. Health")
    axs[1, 0].set_xlabel("Step")
    axs[1, 0].set_ylabel("Average Health")
    axs[1, 0].set_title("Average Life Form Health Over Time")
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    # Average energy
    for species, species_data in life_form_data.items():
        axs[1, 1].plot(steps, species_data["energy"], label=f"{species} Avg. Energy")
    axs[1, 1].set_xlabel("Step")
    axs[1, 1].set_ylabel("Average Energy")
    axs[1, 1].set_title("Average Life Form Energy Over Time")
    axs[1, 1].legend()
    axs[1, 1].grid(True)

    plt.tight_layout()
    plt.savefig("simulation_plot.png")
    plt.show()
