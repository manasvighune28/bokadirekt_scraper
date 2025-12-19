import time
import os

# Base URL of the site you want to scrape
BASE_URL = "https://www.vanityclinics.se"

# Run browser in headless mode (True = no visible window, False = visible for debugging)
HEADLESS = False


# Browser window size
WINDOW_SIZE = "1920,1080"

# Page load timeout in seconds
PAGELOAD_TIMEOUT_SEC = 30

# Default wait time for elements
DEFAULT_WAIT_SEC = 10

# Limit how many booking samples you collect
MAX_BOOKING_SAMPLES = 5

# Output directory
OUTPUT_DIR = "output"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Timestamp for filenames (e.g., vanityclinics_2025-12-11_16-05-33.csv)
TIMESTAMP = time.strftime("%Y-%m-%d_%H-%M-%S")

# File paths for saving results
JSON_FILE = os.path.join(OUTPUT_DIR, f"vanityclinics_{TIMESTAMP}.json")
CSV_FILE = os.path.join(OUTPUT_DIR, f"vanityclinics_{TIMESTAMP}.csv")
