
- **README.md:** Quick notes and commands.
- **requirements.txt:** Dependencies.
- **config.py:** Base URL and driver options.
- **selectors.py:** Centralized locators with fallbacks.
- **parse_utils.py:** Text cleaning and mini-parsers.
- **scraper.py:** Selenium logic.
- **run.py:** Entry point and file save.
- **output/:** JSON data.

---

## Code files

Copy-paste each file exactly. You can tweak later if the site changes wording or structure.

### config.py
```python
BASE_URL = "https://www.bokadirekt.se/places/vanityclinics-46325"

IMPLICIT_WAIT_SEC = 0
PAGELOAD_TIMEOUT_SEC = 60
DEFAULT_WAIT_SEC = 20

HEADLESS = False  # set True for CI/server runs
MAX_BOOKING_SAMPLES = 3
WINDOW_SIZE = "1400,900"

# Bokadirekt VanityClinics scraper

## Create venv
- Windows:
  - `python -m venv .venv`
  - `.venv\Scripts\activate`
- macOS/Linux:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`

## Install
`pip install -r requirements.txt`

## Run
`python run.py`

## Output
`output/vanityclinics.json` with services, try offers, and booking samples (contractors + time slots).
