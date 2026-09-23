from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

import random
import time
from datetime import datetime


URL = "https://www.facebook.com/professional_dashboard/profile_insights/views/?date_range=TODAY&locale=en_GB"

                
while True:
    try:
        with sync_playwright() as p:

            browser = p.chromium.launch_persistent_context(
                "/Users/Code/FacebookReelScraper/auth/facebook_profile",
                headless=True
            )

            page = browser.pages[0] if browser.pages else browser.new_page()

            page.goto(URL, wait_until="domcontentloaded")

            # Get the first value
            text = page.locator("body").inner_text()
            lines = [line.strip() for line in text.splitlines() if line.strip()]

            start = lines.index("Today") + 1
            old_value = lines[start]

            # Keep refreshing until the value changes
            while True:

                time.sleep(random.uniform(60, 90))

                page.reload(wait_until="domcontentloaded")

                text = page.locator("body").inner_text()
                lines = [line.strip() for line in text.splitlines() if line.strip()]

                start = lines.index("Today") + 1
                new_value = lines[start]

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if new_value != old_value:
                    print("Old:", old_value)
                    print("New:", new_value)
                    print("Time: ", timestamp)
                    old_value = new_value
    except Exception:
        pass
