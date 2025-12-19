from playwright.sync_api import sync_playwright

def scrape_vanityclinics():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.bokadirekt.se/places/vanityclinics-46325")

        # Accept cookies
        try:
            page.locator("//button[contains(., 'Tillåt alla cookies')]").click()
            print("✅ Accepted cookies")
        except Exception as e:
            print("⚠️ Cookie button not found:", e)

        # Click "Visa tjänster"
        try:
            page.locator("//button[contains(., 'Visa tjänster')]").click()
            print("✅ Opened services list")
        except Exception as e:
            print("⚠️ Services button not found:", e)

        # Wait for service cards
        try:
            page.wait_for_selector("div[data-testid='service-card']", timeout=20000)
            cards = page.query_selector_all("div[data-testid='service-card']")
            print(f"Found {len(cards)} services")
        except Exception as e:
            print("⚠️ No service cards found:", e)

        browser.close()


if __name__ == "__main__":
    scrape_vanityclinics()



if __name__ == "__main__":
    data = scrape_vanityclinics()
    print(f"\n✅ Scraped {len(data)} services")
