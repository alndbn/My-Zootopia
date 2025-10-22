import json
import html


def load_data(file_path):
    """Load JSON data from the given file path."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Convert one animal entry into an HTML <li> card."""
    def normalize(s):
        return s.replace("’", "'").replace("‘", "'")

    name = normalize(animal.get("name", ""))
    characteristics = animal.get("characteristics", {}) or {}
    diet = normalize(characteristics.get("diet", ""))
    type_ = normalize(characteristics.get("type", ""))
    location = normalize(animal.get("locations", [""])[0])

    name, diet, type_, location = map(html.escape, [name, diet, type_, location])

    return (
        '<li class="cards__item">\n'
        f'  <div class="card__title">{name}</div>\n'
        '  <p class="card__text">\n'
        f'      <strong>Diet:</strong> {diet}<br/>\n'
        f'      <strong>Location:</strong> {location}<br/>\n'
        f'      <strong>Type:</strong> {type_}<br/>\n'
        '  </p>\n'
        '</li>\n'
    )


def generate_html(cards_html, template_path, output_path):
    """Insert the cards into the template and write the final HTML file."""
    with open(template_path, "r", encoding="utf-8") as f:
        template_html = f.read()

    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", cards_html)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    return cards_html.count('<li class="cards__item">')


def main():
    """Generate animals.html from JSON data and template."""
    data_path = "animals_data.json"
    template_path = "animals_template.html"
    output_path = "animals.html"

    animals = load_data(data_path)
    cards_html = "".join(serialize_animal(a) for a in animals)
    li_count = generate_html(cards_html, template_path, output_path)

    print(f"li-count: {li_count}")
    print(f"wrote {output_path}")


if __name__ == "__main__":
    main()
