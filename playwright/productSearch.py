from playwright.sync_api import sync_playwright
import csv

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.mercadolivre.com.br/")
        
        page.fill("input[name='as_word']", "Notebook")
        page.click("button[type='submit']")
        
        page.wait_for_selector("li.ui-search-layout__item", timeout=15000)

        produtos = page.locator("li.ui-search-layout__item")
        resultados = []

        for i in range(min(5, produtos.count())):
            produto = produtos.nth(i)

            try:
                nome = produto.locator("h2.ui-search-item__title, h2, h3").first.inner_text(timeout=5000)
            except:
                nome = "Nome não encontrado"
            try:
                preco = produto.locator("span.andes-money-amount__fraction").first.inner_text(timeout=5000)
            except:
                preco = "Preço não encontrado"

            resultados.append({"nome": nome, "preco": preco})

        with open("produtos.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["nome", "preco"])
            writer.writeheader()
            writer.writerows(resultados)
        
        browser.close()
        print("Dados salvos em produtos.csv")

if __name__ == "__main__":
    main()
