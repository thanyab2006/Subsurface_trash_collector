import csv
import random
import os

# -------------------------------
# CONFIGURATION
# -------------------------------

NUM_RECORDS = 100
OUTPUT_DIR = "data/raw"
OUTPUT_FILE = "trash_dataset.csv"

TRASH_TYPES = ["plastic", "metal", "organic", "glass", "paper"]

# -------------------------------
# DATA GENERATION FUNCTIONS
# -------------------------------

def generate_trash_record(record_id):
    """
    Generates a single simulated trash detection record.
    """
    location_x = round(random.uniform(0, 100), 2)
    location_y = round(random.uniform(0, 100), 2)
    depth_cm = random.randint(10, 300)
    trash_type = random.choice(TRASH_TYPES)
    size_cm = random.randint(5, 100)
    collected = random.choice(["yes", "no"])

    return [
        record_id,
        location_x,
        location_y,
        depth_cm,
        trash_type,
        size_cm,
        collected
    ]


def generate_dataset():
    """
    Generates a CSV dataset for subsurface trash simulation.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow([
            "id",
            "location_x",
            "location_y",
            "depth_cm",
            "trash_type",
            "size_cm",
            "collected"
        ])

        # Data rows
        for i in range(1, NUM_RECORDS + 1):
            writer.writerow(generate_trash_record(i))

    return file_path