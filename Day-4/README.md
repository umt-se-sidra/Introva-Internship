# Day 4 — Playwright: Modern Browser Automation

## What I Learned

- Playwright is a modern browser automation library.
- It can automate Chromium, Firefox, and WebKit.
- Playwright supports both synchronous and asynchronous APIs.
- Its auto-waiting makes dynamic-page automation easier.
- Locators are used to find and interact with page elements.
- Async Playwright uses `async` and `await`.

## Selenium vs Playwright

| Feature | Selenium | Playwright |
|---|---|---|
| Browser automation | Yes | Yes |
| Auto-waiting | Limited/manual waits often needed | Built-in auto-waiting |
| Async API | Less convenient | Strong async support |
| Dynamic websites | Yes | Yes |
| Locators | Yes | Yes |
| Ease of writing | More boilerplate | Generally simpler |
| Best use | Mature/legacy automation and broad ecosystem | Modern dynamic web automation |

## Practical Work

### 1. Dynamic Loading

Used Playwright to:

1. Open a dynamic webpage.
2. Click the Start button.
3. Wait for dynamically loaded content.
4. Extract the result.

Result:

`Hello World!`

### 2. Second Dynamic Site

Built an asynchronous Playwright scraper for:

`https://quotes.toscrape.com/js/`

The scraper:

- Opens the JavaScript-rendered page.
- Finds quote elements.
- Extracts quote text.
- Extracts authors.
- Prints the scraped data.

## Key Learning

Playwright does not automatically replace Selenium in every project. The choice depends on the project requirements, browser support, existing codebase, and automation needs.
