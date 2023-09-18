"""web crawler using breadth-first search"""

from collections import deque
from PySiteCrawler.utils import WebUtils


class BFSWebCrawler:
    """
    A web crawler that uses breadth-first search to crawl the web.
    """

    def __init__(self, base_url, geckodriver_path=None, chromedriver_path=None, max_depth=None, headless=True, disable_file_generation=False):
        self.base_url = base_url
        self.max_depth = max_depth
        self.geckodriver_path = geckodriver_path
        self.chromedriver_path = chromedriver_path
        self.headless = headless
        self.disable_file_generation = disable_file_generation
        self.website_text = {}

    def __website_processor(self, driver, url):
        """
        Process the website.
        """
        print("Processing:", url)
        content = WebUtils.get_page_content(driver, url)
        text, title = WebUtils.extract_text_and_title_from_html(content)
        # save data to a dictionary
        if self.base_url in self.website_text:
            self.website_text[self.base_url] = self.website_text[self.base_url] + text
        else:
            self.website_text[self.base_url] = text

        if not self.disable_file_generation:
            WebUtils.save_text_as_txt(title, text, url)

        links = WebUtils.get_links_from_html(content, url)
        return links

    def crawl(self):
        """
        Perform a breadth-first search on the website.
        """
        try:
            driver = None
            if self.geckodriver_path is None:
                driver = WebUtils.start_chromiumdriver(
                    path=self.chromedriver_path, headless=self.headless)
            elif self.chromedriver_path is None:
                driver = WebUtils.start_geckodriver(
                    path=self.geckodriver_path, headless=self.headless)
            visited_urls = set()
            queue = deque([(self.base_url, 0)])
            visited_urls.add(self.base_url)
            while queue:
                url, depth = queue.popleft()
                if self.max_depth is not None and depth > self.max_depth:
                    break
                links = self.__website_processor(driver, url)
                for link in links:
                    if link not in visited_urls:
                        queue.append((link, depth + 1))
                        visited_urls.add(link)

        except Exception as exception:
            print("An error occurred:", exception)

        finally:
            WebUtils.stop_driver(driver)
