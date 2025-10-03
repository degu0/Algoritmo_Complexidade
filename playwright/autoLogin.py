from playwright.sync_api import sync_playwright
import os

def main():
    with sync_playwright() as p: 
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")
        page.fill("input[id='username']", "tomsmith")
        page.fill("input[id='password']", "SuperSecretPassword!")
        page.click("button[type='submit']")

        assert page.url == "https://the-internet.herokuapp.com/secure"

        page.wait_for_selector(".flash.success")
        page.wait_for_timeout(4000) 
        print("✅ Login realizado com sucesso")

        browser.close()

if __name__ == "__main__":
    main()