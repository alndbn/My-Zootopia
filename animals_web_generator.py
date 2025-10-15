import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")
#print(animals_data)

#iterate through the data loaded from the JSON file and print:
for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("diet")
    locations = animal.get("locations")
    first_location = locations[0] if isinstance(locations, list) and locations else None
    type_ = animal.get("type")

    if name:    print("Name:", name)
    if diet:    print("Diet:", diet)
    if first_location:print("Location:", first_location)
    if type_:    print("Type:", type_)
    print("-" * 40)
