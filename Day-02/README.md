# Day 2 — BeautifulSoup: Static Scraping at Scale

## Objective

Learn how to scrape static websites using Requests and BeautifulSoup, understand HTML page structure and CSS selectors, and scale scraping using asynchronous requests with `httpx` and semaphore-based rate limiting.

## Tasks Completed

* Inspected the HTML structure of `books.toscrape.com`.
* Practiced `find()` and `find_all()` with BeautifulSoup.
* Used CSS selectors to locate elements on web pages.
* Extracted book information from the website.
* Worked with pagination to process multiple pages.
* Used asynchronous HTTP requests with `httpx`.
* Applied semaphore-based rate limiting for responsible concurrent scraping.
* Considered `robots.txt` and web-scraping ethics.
* Used a dataclass pattern for structured extracted data.
* Saved scraped results to CSV.
* Used Pandas to calculate average prices by category.

## Files

* `topics.md` — Topics and concepts learned during Day 2.
* `main.py` — Python implementation of the scraping task.

## Outcome

Built a static web scraper using BeautifulSoup and scaled it to scrape the paginated Books to Scrape website using asynchronous requests while applying responsible scraping practices.
