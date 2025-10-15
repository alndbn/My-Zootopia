import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animal_data = load_data("animals_data.json")
#print(animals_data)

output = ""
#iterate through the data loaded from the JSON file and print:
for animal in animal_data:
    chars = animal.get("characteristics") or {}
    name = animal.get("name")
    diet = chars.get("diet")
    locations = animal.get("locations")
    first_location = locations[0] if isinstance(locations, list) and locations else None
    type_ = chars.get("type")

    if name is not None:
        output += f"Name: {name}\n"
    if diet is not None:
        output += f"Diet: {diet}\n"
    if first_location is not None:
        output += f"Location: {first_location}\n"
    if type_ is not None:
        output += f"Type: {type_}\n"

    output += "\n"

print(output[:400])


with open("animals_template.html", "r") as f:
    template_html = f.read()

final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w", encoding="utf-8") as f:
    f.write(final_html)
print("wrote animals.html")

