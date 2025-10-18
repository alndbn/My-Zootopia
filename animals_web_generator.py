import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

# Daten laden
animal_data = load_data("animals_data.json")

output = ""

for animal in animal_data:

    name = animal.get("name", "")
    name = name.replace("’", "'").replace("‘", "'")

    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet", "")
    type_ = characteristics.get("type", "")
    location = ""
    if "locations" in animal and animal["locations"]:
        location = animal["locations"][0]


    output += (
        '<li class="cards__item">\n'
        f'  <div class="card__title">{name}</div>\n'
        '  <p class="card__text">\n'
        f'      <strong>Diet:</strong> {diet}<br/>\n'
        f'      <strong>Location:</strong> {location}<br/>\n'
        f'      <strong>Type:</strong> {type_}<br/>\n'
        '  </p>\n'
        '</li>\n'
    )

print(output)
print("li-count:", output.count('<li class="cards__item">'))

with open("animals_template.html", "r", encoding="utf-8") as f:
    template_html = f.read()

final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("li-count:", output.count('<li class="cards__item">'))
print("wrote animals.html")
