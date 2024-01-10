import json

def modify_jsonl(file_path, field_to_remove, new_field, new_value):
    try:
        # Read the JSONL file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Process each line (each JSON object)
        updated_lines = []
        for line in lines:
            data = json.loads(line)
            # Remove the specified field if it exists
            if field_to_remove in data:
                del data[field_to_remove]
            # Add the new field
            data[new_field] = new_value
            updated_lines.append(json.dumps(data, ensure_ascii=False) + '\n')

        # Write the updated data back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Sample usage
file_path = 'theorem_proving_zh.jsonl'
field_to_remove = 'idx_before_set'
new_field = 'version'
new_value = 'v0.0.1'
modify_jsonl(file_path, field_to_remove, new_field, new_value)
