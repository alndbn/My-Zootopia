import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

# Daten laden
animal_data = load_data("animals_data.json")


output = ""

for animal in animal_data:
    output += '<li class="cards__item">\n'

    if "name" in animal:
        output += f"Name: {animal['name']}<br/>\n"

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}<br/>\n"

    if "locations" in animal and animal["locations"]:
        output += f"Location: {animal['locations'][0]}<br/>\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}<br/>\n"

    output += "</li>\n"


print(output)
print("li-count:", output.count('<li class="cards__item">'))


with open("animals_template.html", "r", encoding="utf-8") as f:
    template_html = f.read()

final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("li-count:", output.count('<li class="cards__item">'))
print("wrote animals.html")

