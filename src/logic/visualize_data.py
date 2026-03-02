import csv
import os
import matplotlib.pyplot as plt

OUTPUT_DIR = "data/processed"

def visualize_dataset(file_path):
    """
    Generates basic visualizations from the trash dataset.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    trash_type_counts = {}
    depths = []

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            trash_type = row["trash_type"]
            depth = int(row["depth_cm"])

            trash_type_counts[trash_type] = trash_type_counts.get(trash_type, 0) + 1
            depths.append(depth)

    # -------------------------------
    # Bar Chart: Trash Types
    # -------------------------------
    plt.figure()
    plt.bar(trash_type_counts.keys(), trash_type_counts.values())
    plt.title("Trash Type Distribution")
    plt.xlabel("Trash Type")
    plt.ylabel("Count")
    plt.savefig(f"{OUTPUT_DIR}/trash_type_distribution.png")
    plt.close()

    # -------------------------------
    # Histogram: Depth Distribution
    # -------------------------------
    plt.figure()
    plt.hist(depths, bins=10)
    plt.title("Trash Depth Distribution")
    plt.xlabel("Depth (cm)")
    plt.ylabel("Frequency")
    plt.savefig(f"{OUTPUT_DIR}/trash_depth_distribution.png")
    plt.close()

    print("\n📈 Visualizations saved to data/processed/")