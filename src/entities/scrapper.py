from bs4 import BeautifulSoup
import requests


class Scrapper:
    
    def __init__(self, url) -> None:
        self.url:str = url
    
    def scrapper_parser(self, url) -> object:
        response = requests.get(url)
        html = response.text
        return BeautifulSoup(html, 'html.parser').prettify()