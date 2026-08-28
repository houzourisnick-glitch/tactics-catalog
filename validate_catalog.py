import json
import sys
from pathlib import Path
from jsonschema import validate

def main():
    try:
        base_dir = Path(__file__).parent
        schema_path = base_dir / 'tactic.schema.json'
        catalog_path = base_dir / 'CI_TACTICS_CATALOG_v3.0.json'

        with open(schema_path, 'r', encoding='utf-8') as sf:
            schema = json.load(sf)
        with open(catalog_path, 'r', encoding='utf-8') as sf:
            catalog_data = json.load(sf)

        # Handle both root-level lists and object containers with metadata
        if isinstance(catalog_data, dict):
            tactics_list = None
            for key, value in catalog_data.items():
                if isinstance(value, list):
                    tactics_list = value
                    break
            if tactics_list is None:
                raise ValueError("Could not find a list of tactics inside the catalog object.")
        elif isinstance(catalog_data, list):
            tactics_list = catalog_data
        else:
            raise ValueError("Catalog JSON root must be an object or a list.")

        validated_count = 0
        for idx, tactic in enumerate(tactics_list):
            if isinstance(tactic, dict) and "tactic_id" in tactic:
                validate(instance=tactic, schema=schema)
                validated_count += 1

        print(f"Validation successful: All {validated_count} tactics match schema.")
    except Exception as e:
        print(f"Validation failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()