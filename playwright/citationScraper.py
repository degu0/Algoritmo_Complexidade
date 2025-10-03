from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://quotes.toscrape.com")
        page.wait_for_timeout(1000)

        citacoes = page.locator(".text")
        authors = page.locator(".author")

        count = citacoes.count()
        print(f"Encontradas {count} citações:")

        for i in range(count):
            citacao = citacoes.nth(i).inner_text()
            author = authors.nth(i).inner_text()
            print(f"{citacao} by {author}")

        browser.close()

if __name__ == "__main__":
    main()
