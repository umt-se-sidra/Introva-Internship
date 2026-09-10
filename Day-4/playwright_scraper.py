import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        page = await browser.new_page()

        await page.goto(
            "https://the-internet.herokuapp.com/dynamic_loading/1"
        )

        print("Page opened")

        # Click the Start button
        await page.locator("#start button").click()

        print("Start button clicked")

        # Wait for the dynamically loaded text
        text = await page.locator("#finish h4").inner_text()

        print("Result:", text)

        await page.wait_for_timeout(3000)

        await browser.close()


asyncio.run(main())
