# scraper/scraper.py
from playwright.sync_api import sync_playwright

def scrape_chapter():
    url =("https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.locator("#mw-content-text").inner_text()
        page.screenshot(path="chapter1.png")
        with open("chapter1.txt", "w", encoding="utf-8") as f:
            f.write(content)
        browser.close()
    return content

if __name__ == "__main__":
    text = scrape_chapter()
    print("Scraped chapter saved to chapter1.txt")
