import json
import sys
from jsonschema import validate

def main():
    try:
        with open('tactic.schema.json', 'r', encoding='utf-8') as sf:
            schema = json.load(sf)
        with open('CI_TACTICS_CATALOG_v3.0.json', 'r', encoding='utf-8') as sf:
            catalog = json.load(sf)

        for idx, tactic in enumerate(catalog):
            validate(instance=tactic, schema=schema)
        print(f"Validation successful: All {len(catalog)} tactics match schema.")
    except Exception as e:
        print(f"Validation failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()