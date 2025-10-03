from playwright.sync_api import sync_playwright
import os

def main():
    with sync_playwright() as p: 
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.youtube.com")
        page.fill("input[name='search_query']", "MrsBeast")
        page.keyboard.press("Enter")

        page.wait_for_timeout(4000) 

        screenshots_dir = "screenshots_saucedemo"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        screenshot1_path = os.path.join(screenshots_dir, "01_login_page.png")
        page.screenshot(path=screenshot1_path, full_page=True)
        print(f"📸 Screenshot salvo: {screenshot1_path}")
        

        browser.close()

if __name__ == "__main__":
    main()