"""Setup script for PySiteCrawler."""

from setuptools import setup

setup(
    name='PySiteCrawler',
    version='0.0.1',
    description='A web crawler that uses graph traversal algorithms to crawl the web.',
    author='Arghyadeep Ghosh',
    author_email='imarghyadeep@gmail.com',
    url='https://github.com/Arghya721/PySiteCrawler',
    packages=['PySiteCrawler','PySiteCrawler.crawler','PySiteCrawler.crawler'],
    install_requires=['selenium==4.7.2','urllib3==1.26.6','html2text==2020.1.16','beautifulsoup4==4.11.2'],
)
