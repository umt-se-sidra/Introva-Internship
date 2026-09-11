# Day 5 — Scrapy + Crawl4AI + Pandas

## Topic

**Scrapy + Crawl4AI — Frameworks & AI-Assisted Extraction**

## What I Learned

* Scrapy's spider, item, and pipeline structure
* Creating a basic Scrapy spider
* Exporting scraped data to JSON
* Crawl4AI for extracting structured information from web pages
* Using schema-based extraction
* Cleaning scraped data with Pandas
* Removing duplicate records
* Checking and handling missing values
* Standardizing scraped data
* Exporting a clean CSV dataset

## Part 1 — Scrapy

Created a minimal Scrapy spider to understand the basic Scrapy workflow.

### Practical Task

* Scaffold a simple Scrapy spider
* Scrape data from a webpage
* Export the results as JSON

## Part 2 — Crawl4AI

Used Crawl4AI to extract structured information from an article/web page.

### Practical Task

* Crawl a webpage using Crawl4AI
* Extract selected structured fields
* Work with schema/LLM-assisted extraction

## Final Dataset — Pandas

Cleaned the week's complete scraped dataset using Pandas.

### Cleaning Steps

* Loaded the scraped CSV
* Checked dataset shape and columns
* Checked for missing values
* Checked for duplicate rows
* Calculated average price by category
* Exported the cleaned dataset

### Final Dataset

* Records: 1000
* Columns: 4
* Missing values: 0
* Duplicate rows: 0
* Output file: `cleaned_books.csv`

## Scraping Approaches Covered

During the week, I worked with five different scraping approaches:

1. Requests + BeautifulSoup — static pages
2. Selenium — browser automation
3. Playwright — modern browser automation
4. Scrapy — structured crawling framework
5. Crawl4AI — AI-assisted structured extraction

## Outcome

By the end of Day 5, I understand the main scraping approaches and when each approach is useful. I also have a cleaned dataset that can be used for further analysis or the capstone project.
