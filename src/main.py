from simulation.generate_dataset import generate_dataset

def main():
    print("Starting Subsurface Trash Collector Simulation...\n")

    dataset_path = generate_dataset()

    print("Simulation complete.")
    print(f"Dataset saved at: {dataset_path}")


if __name__ == "__main__":
    main()