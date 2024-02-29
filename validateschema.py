import json
import jsonschema

def validate_json(file_path, schema_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    
    with open(schema_path) as schema_file:
        schema = json.load(schema_file)

    validator = jsonschema.Draft7Validator(schema)
    errors = validator.iter_errors(data)

    for error in errors:
        print(f"File: {file_path} Error: {error.message})
    
    if len(errors) == 0:
        print(f'No errors found in file {file_path}')

validate_json("json-test-1.json", "schema.json")
validate_json("json-test-2.json", "schema.json")