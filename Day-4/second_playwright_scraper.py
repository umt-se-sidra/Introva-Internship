import asyncio
from playwright.async_api import async_playwright


async def scrape_quotes():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        page = await browser.new_page()

        await page.goto("https://quotes.toscrape.com/js/")

        # Wait for quotes to appear
        quotes = page.locator(".quote")

        count = await quotes.count()

        print("Total quotes:", count)

        for i in range(count):
            quote = quotes.nth(i)

            text = await quote.locator(".text").inner_text()
            author = await quote.locator(".author").inner_text()

            print(f"{i + 1}. {text} — {author}")

        await browser.close()


asyncio.run(scrape_quotes())
