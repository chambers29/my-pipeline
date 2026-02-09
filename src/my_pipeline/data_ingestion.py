from .config import BASE_DIR, DATA_DIR
from pathlib import Path
import random
import datetime


# Data ingestion function

def generate_data(output_file:str, num_entries:int):
    print(f"{datetime.datetime.now()} Generating data to \"{output_file}\"...")

    output = Path(f"{DATA_DIR}/{output_file}")

    with open (output, "w") as f:
        for i in range(num_entries):
            f.write(f"{i * random.randint(1, 100)}\n")

    print(f"{datetime.datetime.now()} Data generation complete.")
    return output