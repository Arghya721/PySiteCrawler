"""web crawler using depth-first search"""

from PySiteCrawler.utils import WebUtils

class DFSWebCrawler:
    """
    A web crawler that uses depth-first search to crawl the web.
    """

    def __init__(self, base_url, geckodriver_path=None, chromedriver_path=None, max_depth=None, headless=True):
        self.base_url = base_url
        self.max_depth = max_depth
        self.geckodriver_path = geckodriver_path
        self.chromedriver_path = chromedriver_path
        self.headless = headless

    def __website_processor(self , driver, url):
        """
        Process the website.
        """
        content = WebUtils.get_page_content(driver, url)
        text, title = WebUtils.extract_text_and_title_from_html(content)
        WebUtils.save_text_as_txt(title, text, url)
        links = WebUtils.get_links_from_html(content, url)
        return links
    
    def __dfs(self, driver, url, depth, visited_urls):
        """
        Perform a depth-first search on the website.
        """

        if self.max_depth is not None and depth > self.max_depth:
            return

        links = self.__website_processor(driver, url)
        for link in links:
            if link not in visited_urls:
                visited_urls.add(link)
                self.__dfs(driver, link, depth + 1, visited_urls)
    
    def crawl(self):
        """crawl the website"""
        try:
            driver = None
            if self.geckodriver_path is None:
                driver = WebUtils.start_chromiumdriver(path=self.chromedriver_path , headless=self.headless)
            elif self.chromedriver_path is None:
                driver = WebUtils.start_geckodriver(path=self.geckodriver_path , headless=self.headless)
            visited_urls = set()
            visited_urls.add(self.base_url)
            self.__dfs(driver, self.base_url, 0, visited_urls)
        
        except Exception as exception:
            print("An error occurred:", exception)
        
        finally:
            WebUtils.stop_driver(driver)