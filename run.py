import csv
import time
from scraper import scrape_all

if __name__ == "__main__":
    data = scrape_all()

    # Timestamped filename
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output/vanityclinics_{timestamp}.csv"

    # Expanded fieldnames to include metadata
    fieldnames = [
        "scraped_at", "place", "url", "type", "tab",
        "title", "duration", "price", "description",
        "book_url", "contractor_name", "slot"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        # Services + Try offers
        for group, label in [(data.get("services", []), "service"),
                             (data.get("try_offers", []), "try_offer")]:
            for s in group:
                writer.writerow({
                    "scraped_at": data.get("scraped_at", ""),
                    "place": data.get("place", ""),
                    "url": data.get("url", ""),
                    "type": label,
                    "tab": s.get("tab", ""),
                    "title": s.get("title", ""),
                    "duration": s.get("duration", ""),
                    "price": s.get("price", ""),
                    "description": s.get("description", ""),
                    "book_url": s.get("book_url", ""),
                    "contractor_name": "",
                    "slot": ""
                })

        # Booking samples → flatten contractors and slots into separate rows
        for b in data.get("booking_samples", []):
            # Contractors
            for c in b.get("contractors", []):
                writer.writerow({
                    "scraped_at": data.get("scraped_at", ""),
                    "place": data.get("place", ""),
                    "url": data.get("url", ""),
                    "type": "booking_sample",
                    "tab": "",
                    "title": b.get("service_title", ""),
                    "duration": "",
                    "price": "",
                    "description": "",
                    "book_url": b.get("book_url", ""),
                    "contractor_name": c.get("name", ""),
                    "slot": ""
                })
            # Slots
            for s in b.get("slots", []):
                writer.writerow({
                    "scraped_at": data.get("scraped_at", ""),
                    "place": data.get("place", ""),
                    "url": data.get("url", ""),
                    "type": "booking_sample",
                    "tab": "",
                    "title": b.get("service_title", ""),
                    "duration": "",
                    "price": "",
                    "description": "",
                    "book_url": b.get("book_url", ""),
                    "contractor_name": "",
                    "slot": s
                })

    print(f"✅ Scraping complete. Results saved to {filename}")
