from .config import BASE_DIR, DATA_DIR
import datetime
from pathlib import Path


# Data validation script
def validate_data(data_file:str, output_file:str):
    print(f"{datetime.datetime.now()} Validating data from \"{data_file}\"...")
    output = Path(f"{DATA_DIR}/{output_file}")

    with open(data_file, "r") as in_f:
        with open(output, "w") as out_f:
            invalid_count = 0
            for line in in_f:
                value = int(line.strip())
                if value % 777 != 0 or value == 0:
                    invalid_count += 1
                else:
                    out_f.write(f"{value}\n")

    print(f"{datetime.datetime.now()} Validation complete. Found {invalid_count} invalid entries.")
    return output