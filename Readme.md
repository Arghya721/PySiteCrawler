# PySiteCrawler - A Simple Web Crawling Library

PySiteCrawler is a Python library designed for web crawling and data extraction, offering a simple and efficient way to explore web pages, extract text content, and manage links during the crawling process. The library is designed to provide versatile traversal methods, with additional traversal strategies planned for future updates. All scraped data is conveniently stored in .txt files for easy access and analysis.

## Features

- Breadth-First Search Crawling: Seamlessly traverse websites using a breadth-first search strategy.

- Depth-First Search Crawling: Efficiently explore websites using a depth-first search strategy.

- Text Extraction: Extract text content and titles from HTML pages for further analysis.

- Headless Browsing: Use either GeckoDriver or ChromeDriver for headless browsing.


## Prerequisites

Before using PySiteCrawler, ensure that you have the following prerequisites in place:

- **Python**: PySiteCrawler requires Python (version 3.6 or higher). You can download the latest version of Python from [here](https://www.python.org/downloads/).

- **WebDriver Setup**:
  - **GeckoDriver**: For Firefox browser automation, download the latest GeckoDriver from [here](https://github.com/mozilla/geckodriver/releases) and make sure it is available in your system's PATH.
  - **ChromeDriver**: For Chrome browser automation, download the latest ChromeDriver from [here](https://chromedriver.chromium.org/downloads) and make sure it is available in your system's PATH.

## Installation

You can easily install PySiteCrawler using pip:

```bash
pip install PySiteCrawler
```

## Classes and Functions

### BFSWebCrawler

The `BFSWebCrawler` class provides the following functions and methods:

- `__init__(base_url, geckodriver_path=None, chromedriver_path=None, max_depth=None, headless=False)`: Initialize the BFSWebCrawler instance.
- `crawl()`: Perform a breadth-first search crawl on the specified website.


### DFSWebCrawler

The `DFSWebCrawler` class provides the following functions and methods:

- `__init__(base_url, geckodriver_path=None, chromedriver_path=None, max_depth=None, headless=False)`: Initialize the DFSWebCrawler instance.
- `crawl()`: Perform a depth-first search crawl on the specified website.

**Note: The Selenium driver used for crawling has a default timeout of 10 seconds per page.**

## Usage

Here's a quick example of how to use PySiteCrawler to perform a breadth-first search crawl on a website:

```bash
from PySiteCrawler.crawler.bfs_web_crawler import BFSWebCrawler

# Initialize a BFSWebCrawler
crawler = BFSWebCrawler("https://example.com", max_depth=2,
                         geckodriver_path=r"path/to/geckodriver")
crawler.crawl()
```

You can also specify the chromedriver_path parameter during initialization to use the ChromeDriver for crawling. (It is suggested to use the geckodriver as chromedriver causes some issue in loading the website correctly in headless mode)

```bash
from PySiteCrawler.crawler.dfs_web_crawler import DFSWebCrawler

# Initialize a DFSWebCrawler
crawler = DFSWebCrawler("https://example.com", max_depth=2,
                         chromedriver_path=r"path/to/chromedriver")
crawler.crawl()
```

You can get all the text for all the visited page using website_text dictionary.

```
text = crawler.website_text["https://example.com"]
```

Pass the base url to get all the crawled website text data.

### Parameters

- `base_url`: The starting URL for web crawling.
- `max_depth` (optional): The maximum depth of crawling. Default is None (no limit).
- `geckodriver_path` (optional): Path to GeckoDriver executable for Firefox. Default is None (uses ChromeDriver).
- `chromedriver_path` (optional): Path to ChromeDriver executable for Chrome. Default is None (uses GeckoDriver).
- `headless` (optional): If `True`, the browser will run in headless mode (no GUI display). If `False`, the browser GUI will be visible. Default is `True`.
- `disable_file_generation`(optional): If `False`, all the text content for each visited page will be stored into a .txt file. Default is `False`. 

> **Note**: The `base_url` parameter and either `geckodriver_path` or `chromedriver_path` are necessary for PySiteCrawler to work correctly. Specify the appropriate WebDriver path based on your preferred browser automation. If `geckodriver_path` is provided, GeckoDriver will be used by default. If `chromedriver_path` is provided, ChromeDriver will be used for crawling. It is suggested to use GeckoDriver, as ChromeDriver may cause issues in loading websites correctly in headless mode.


## Contribution

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.