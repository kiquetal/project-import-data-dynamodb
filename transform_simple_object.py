import json

# Create a Python dictionary representing the JSON object
data = {
    "Item": {
        "Dimensions": {
            "S": "8.5 x 11.0 x 1.5"
        },
        "Title": {
            "S": "Book 103 Title"
        },
        "Space": {
             "SS":["HOLA,QUE,TAL"]
            }
    }
}


def extract_values(dictionary):
    values = {}
    for key, value in dictionary.items():
        if isinstance(value,dict):
            values[key]=extract_values(value)
        else:
            print("no dict,print raw value")
            return value
    return values


# Extract values without the "S" or "N" keys
extracted_data = extract_values(data["Item"])

# Convert the extracted data to JSON
json_object = json.dumps(extracted_data, indent=4)

# Print the JSON object
print(json_object)

