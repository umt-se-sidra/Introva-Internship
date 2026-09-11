import asyncio
import json

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai import JsonCssExtractionStrategy


url = "https://quotes.toscrape.com/"


schema = {
    "name": "Quote",
    "baseSelector": ".quote",
    "fields": [
        {
            "name": "text",
            "selector": ".text",
            "type": "text"
        },
        {
            "name": "author",
            "selector": ".author",
            "type": "text"
        },
        {
            "name": "tags",
            "selector": ".tags .tag",
            "type": "text",
            "multiple": True
        }
    ]
}


async def main():

    extraction_strategy = JsonCssExtractionStrategy(schema)

    config = CrawlerRunConfig(
        extraction_strategy=extraction_strategy
    )

    async with AsyncWebCrawler() as crawler:

        result = await crawler.arun(
            url=url,
            config=config
        )

        print("Crawl successful:", result.success)

        if result.extracted_content:
            data = json.loads(result.extracted_content)

            print("\nStructured quote data:")
            print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
