import requests
from bs4 import BeautifulSoup

from parser import MovieParser
from utils import ScraperUtils, DataState

EXCLUDED_SCRIPTS = ["A.I.", "Batman-Begins", "Batman-Forever", ]

class MovieScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            return None

    def scrape_scripts(self):
        html = self.fetch_page(self.base_url)
        script_links = MovieParser.parse_script_links(html)
        errors = []
        for script_name, link in sorted(script_links.items())[:15]:
            try:
                script_html = self.fetch_page(link)
                if script_html is None: continue
                parsed_script = MovieParser.parse_script_content(script_html)
                ScraperUtils.write_list_to_file(script_name, parsed_script, data_state=DataState.RAW)
                standard_script = MovieParser.standardize_script(parsed_script)
                ScraperUtils.write_list_to_file(script_name, standard_script, data_state=DataState.PROCESSED)
            except Exception as e:
                errors.append((script_name, str(e)))
        if errors:
            print("Errors occurred while processing the following scripts:")
            for script_name, error in errors:
                print(f"\"{script_name}\" -> {error}")
        return
    
def main():
    base_url = 'https://imsdb.com/all-scripts.html'  # Replace with the actual URL
    scraper = MovieScraper(base_url)
    scraper.scrape_scripts()

if __name__ == '__main__':  
    main()
