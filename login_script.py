from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir="auth/facebook_profile",
        headless=False
    )

    page = browser.new_page()

    page.goto("https://facebook.com")

    print("Log in manually.")
    input("Press ENTER once you're logged in...")

    browser.close()
