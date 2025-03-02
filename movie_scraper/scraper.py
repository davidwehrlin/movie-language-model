import requests
from bs4 import BeautifulSoup

class MovieScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def parse_script_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for a_tag in soup.find_all('a', href=True):
            if 'script' in a_tag.text.lower():
                links.append(a_tag['href'])
        return links

    def scrape_scripts(self):
        html = self.fetch_page(self.base_url)
        script_links = self.parse_script_links(html)
        scripts = []
        for link in script_links:
            script_html = self.fetch_page(link)
            scripts.append(script_html)
        return scripts