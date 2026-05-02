"""
Prompts user for an animal name, fetches data via data_fetcher,
and generates an HTML page that displays the search results.
"""

import html
import data_fetcher

TEMPLATE_FILE = 'animals_template.html'
OUTPUT_FILE = 'animals.html'
PLACEHOLDER = '__REPLACE_ANIMALS_INFO__'


def serialize_animal(animal):
    """Return an HTML <div> string describing a single animal."""
    name = animal.get('name', 'Unknown')
    characteristics = animal.get('characteristics', {}) or {}
    locations = animal.get('locations', []) or []

    diet = characteristics.get('diet')
    animal_type = characteristics.get('type')
    location = locations[0] if locations else None

    output = '<div class="cards__item">\n'
    output += f'  <h2>{html.escape(name)}</h2>\n'
    output += '  <ul>\n'
    if diet:
        output += f'    <li><strong>Diet:</strong> {html.escape(diet)}</li>\n'
    if location:
        output += f'    <li><strong>Location:</strong> {html.escape(location)}</li>\n'
    if animal_type:
        output += f'    <li><strong>Type:</strong> {html.escape(animal_type)}</li>\n'
    output += '  </ul>\n'
    output += '</div>\n'
    return output


def build_animals_html(animals, animal_name):
    """
    Build the HTML fragment that goes inside the cards container.
    If the API returned no animals, return a friendly error block instead.
    """
    if not animals:
        return (
            f'<div class="error">'
            f'<h2>The animal "{html.escape(animal_name)}" doesn\'t exist.</h2>'
            f'<p>Try a different search term.</p>'
            f'</div>'
        )
    return ''.join(serialize_animal(a) for a in animals)


def generate_website(animal_name):
    """Fetch data, render the template, and write animals.html."""
    animals = data_fetcher.fetch_data(animal_name)

    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()

    animals_html = build_animals_html(animals, animal_name)
    final_html = template.replace(PLACEHOLDER, animals_html)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f'Website was successfully generated to the file {OUTPUT_FILE}.')


def main():
    animal_name = input('Enter a name of an animal: ').strip()
    if not animal_name:
        print('No animal name entered. Exiting.')
        return
    generate_website(animal_name)


if __name__ == '__main__':
    main()
