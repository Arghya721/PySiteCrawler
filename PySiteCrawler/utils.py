"""This file contains utility functions for web scraping"""

import os
import re
from urllib.parse import urlparse, urljoin
import html2text
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
import uuid


class WebUtils:
    """Utility functions for web scraping"""
    @staticmethod
    def get_page_content(driver, url):
        """Get the content of a webpage using Selenium"""
        driver.get(url)
        return driver.page_source

    @staticmethod
    def start_geckodriver(path, headless):
        """Start a Selenium driver"""
        service = FirefoxService(path)
        options = Options()
        options.headless = headless
        driver = webdriver.Firefox(service=service, options=options)
        return driver
    
    @staticmethod
    def start_chromiumdriver(path, headless):
        """Start a Selenium driver"""
        service = ChromeService(executable_path=path)
        options = ChromeOptions()
        options.headless = headless
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    @staticmethod
    def stop_driver(driver):
        """Stop a Selenium driver"""
        driver.quit()

    @staticmethod
    def extract_text_and_title_from_html(content):
        """Extract text and title from HTML content"""
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.title.string.strip() if soup.title else "untitled"
        print("Processing:", title)
        text_converter = html2text.HTML2Text()
        text_converter.ignore_links = True
        text_converter.body_width = 0
        text_converter.skip_internal_links = True
        text_converter.ignore_images = True
        text = text_converter.handle(content)
        return text, title

    @staticmethod
    def sanitize_filename(filename):
        """
        Remove characters that are not allowed in Windows filenames.
        """
        return re.sub(r'[<>:"/\\|?*]', '', filename)

    @staticmethod
    def save_text_as_txt(title, text, base_url):
        """
        Save the text as a .txt file.
        """
        sanitized_title = WebUtils.sanitize_filename(title)
        filename = sanitized_title + str(uuid.uuid1())
        base_url = urlparse(base_url).netloc
        if not os.path.exists(base_url):
            os.makedirs(base_url)
        with open(f"{base_url}/{filename}.txt", "w", encoding="utf-8") as f:
            f.write(text)

    @staticmethod
    def get_links_from_html(content, base_url):
        """
        Get all the links from the HTML content.
        """
        soup = BeautifulSoup(content, 'html.parser')
        links = []
        for link in soup.find_all("a"):
            next_url = link.get("href")
            if not next_url:
                continue
            if not next_url.startswith(('http://', 'https://')):
                next_url = urljoin(base_url, next_url)
            parsed_url = urlparse(next_url)._replace(fragment='').geturl()
            if base_url in parsed_url:
                parsed_url = parsed_url.rstrip('/')
                links.append(parsed_url)
        return links
