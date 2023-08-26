"""Setup script for PySiteCrawler."""

from pathlib import Path
from setuptools import setup


ROOT_DIR = Path(".")

with open(str(ROOT_DIR / "Readme.md")) as readme:
    long_description = readme.read()

setup(
    name='PySiteCrawler',
    version='0.1.2',
    description='A web crawler that uses graph traversal algorithms to crawl the web.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Arghyadeep Ghosh',
    author_email='imarghyadeep@gmail.com',
    url='https://github.com/Arghya721/PySiteCrawler',
    packages=['PySiteCrawler', 'PySiteCrawler.crawler'],
    install_requires=['selenium==4.7.2', 'urllib3==1.26.6',
                      'html2text==2020.1.16', 'beautifulsoup4==4.11.2'],
)
