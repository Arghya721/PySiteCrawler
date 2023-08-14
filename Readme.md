# PySiteCrawler - A Simple Web Crawling Library

PySiteCrawler is a Python library designed for web crawling and data extraction,  offering a simple and efficient way to explore web pages, extract text content, and manage links during the crawling process. The library is designed to provide versatile traversal methods, with additional traversal strategies planned for future updates.


## Features

• Breadth-First Search Crawling: Seamlessly traverse websites using a breadth-first search strategy.

• Text Extraction: Extract text content and titles from HTML pages for further analysis.

• Link Management: Collect and manage links during crawling for comprehensive exploration.
  Headless Browsing: Use either GeckoDriver or ChromeDriver for headless browsing.


## Prerequisites

Before using PySiteCrawler, ensure that you have set up the appropriate WebDriver for your preferred browser:

- **GeckoDriver**: For Firefox browser automation, download the latest GeckoDriver from [here](https://github.com/mozilla/geckodriver/releases) and make sure it is available in your system's PATH.

- **ChromeDriver**: For Chrome browser automation, download the latest ChromeDriver from [here](https://chromedriver.chromium.org/downloads) and make sure it is available in your system's PATH.

## Installation

You can easily install PySiteCrawler using pip:

```bash
pip install PySiteCrawler
```

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
from PySiteCrawler.crawler.bfs_web_crawler import BFSWebCrawler

# Initialize a BFSWebCrawler
crawler = BFSWebCrawler("https://example.com", max_depth=2,
                         chromedriver_path=r"path/to/chromedriver")
crawler.crawl()
```

## Contribution

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.




