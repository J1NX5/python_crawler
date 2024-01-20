import scrapy
import sqlite3
from scrapy_selenium import SeleniumRequest

class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['tagesschau.de']
    start_urls = ['https://tagesschau.de']
  
    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)

        # Erstelle eine SQLite-Datenbank und eine Tabelle, wenn sie noch nicht existiert
        self.conn = sqlite3.connect('foundlinks.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT
            )
        ''')
        self.conn.commit()

    def start_requests(self):
        yield SeleniumRequest(url=self.start_urls[0], callback=self.parse)
        

    def parse(self, response):
        # Hier kannst du auf den gerenderten HTML-Code zugreifen, der auch JavaScript enthält
        # response.text enthält den HTML-Code nach der Ausführung von JavaScript
        # self.log(response.text)
        links = response.css('a::attr(href)').extract()

        # Gib die extrahierten Links aus
        for link in links:
            if link.startswith(('http', 'https', '/')) and not link.startswith(('javascript:', '#')):
                if link.startswith(('/')):
                    link = self.start_urls[0] + link
                print(f'Gefundener Link: {link}')
                # self.log() ist scrapy spezifisch
                # self.log(f'Gefundener Link: {link}')
                if not self.test_link_exist(link):
                    self.c.execute('INSERT INTO links (url) VALUES (?)', (link,))
                    self.conn.commit()
                else:
                    pass
    
    def closed(self, reason):
        self.conn.close()

    def test_link_exist(self,link):
        self.c.execute('SELECT EXISTS(SELECT 1 FROM links WHERE url = ?)', (link,))
        result = self.c.fetchone()[0]
        return result == 1
