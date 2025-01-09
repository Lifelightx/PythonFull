import json

# Load the JSON file
with open('myfile.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract records
records = data.get('records', [])

# Organize data into a hierarchical structure
hierarchy = {}

for record in records:
    state_name = record['state_name_english'].strip()
    district_name = record['district_name_english'].strip()
    subdistrict_name = record['subdistrict_name_english'].strip()

    if state_name not in hierarchy:
        hierarchy[state_name] = {}

    if district_name not in hierarchy[state_name]:
        hierarchy[state_name][district_name] = []

    hierarchy[state_name][district_name].append(subdistrict_name)

# Display the hierarchy
output_file = r'outputfile.txt'

with open(output_file, 'w', encoding='utf-8') as f:
    for state, districts in hierarchy.items():
        f.write(f"State: {state}\n")
        for district, subdistricts in districts.items():
            f.write(f"  District: {district}\n")
            for subdistrict in subdistricts:
                f.write(f"    Sub-district: {subdistrict}\n")

print(f"Hierarchy written to {output_file}")