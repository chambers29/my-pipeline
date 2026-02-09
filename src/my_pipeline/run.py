from .data_ingestion import generate_data
from .data_validation import validate_data

def main():
        # Step 1: Generate data
        raw_data_file = generate_data("raw_data.txt", 1000)

        # Step 2: Validate data
        validated_data_file = validate_data(raw_data_file, "validated_data.txt")

        print("Pipeline finished successfully.")

if __name__ == "__main__":
    main()