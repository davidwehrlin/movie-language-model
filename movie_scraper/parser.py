from bs4 import BeautifulSoup

MIN_COUNT = 100000000000000000000000000000000

class MovieParser:
    
    @staticmethod
    def parse_script_links(html):
        soup = BeautifulSoup(html, 'html.parser')
        links = {}
        for a_tag in soup.find_all('a', href=True):
            href_text = a_tag['href']
            if 'Movie Scripts' in href_text:
                script_name = href_text.split('/')[-1].replace(' ', '-').replace("-Script.html", "")
                links[script_name] = f'https://imsdb.com/scripts/{script_name}.html'  
        return links

    @staticmethod
    def parse_script_content(html):
         soup = BeautifulSoup(html, 'html.parser')
         src_html = soup.find('td', class_='scrtext')
         script_text = src_html.text
         text_lines = script_text.split('\r\n')
         if len(text_lines) < 200:
             raise ValueError("Script content is too short to be valid.")
         return text_lines