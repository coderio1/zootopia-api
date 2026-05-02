# Animals Web Generator

A small Python program that fetches animal information from the
[API Ninjas Animals API](https://api-ninjas.com/api/animals) and generates
a static HTML page displaying the results.

## Features

- Interactive: prompts the user for an animal name at runtime.
- API-backed: fetches live data instead of using a local JSON file.
- Friendly error message in the generated page when no animals are found.
- Clean separation between data fetching (`data_fetcher.py`) and
  website generation (`animals_web_generator.py`).
- API key managed via a `.env` file — never committed to the repository.

## Project structure

```
.
├── animals_web_generator.py   # Main script (orchestrator)
├── data_fetcher.py            # Handles all API communication
├── animals_template.html      # HTML template
├── requirements.txt           # Python dependencies
├── .env                       # .env file
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd animals_web_generator
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate          # macOS / Linux
   venv\Scripts\activate             # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Get a free API key at [api-ninjas.com](https://api-ninjas.com/) and create
   a `.env` file in the project root:
   ```
   API_KEY='your-api-ninjas-key-here'
   ```

## Usage

Run the script:

```bash
python3 animals_web_generator.py
```

You will be prompted for an animal name. After the program finishes,
open `animals.html` in your browser.

Example session:

```
$ python3 animals_web_generator.py
Enter a name of an animal: Fox
Website was successfully generated to the file animals.html.
```

If the animal does not exist in the API's database, the generated page
will display a friendly error message instead of an empty list.

## Dependencies

- [`requests`](https://pypi.org/project/requests/) — HTTP client
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) — loads `.env` into environment variables
