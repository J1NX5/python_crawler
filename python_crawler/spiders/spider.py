import scrapy
from scrapy_selenium import SeleniumRequest

class MySpider(scrapy.Spider):
    name = 'my_spider'

    def start_requests(self):
        # Hier kannst du die URL deiner Zielwebsite angeben
        url = 'https://www.tagesschau.de/'
        
        # SeleniumRequest wird verwendet, um JavaScript auf der Seite auszuführen
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        # Hier kannst du auf den gerenderten HTML-Code zugreifen, der auch JavaScript enthält
        # response.text enthält den HTML-Code nach der Ausführung von JavaScript
        # self.log(response.text)
        links = response.css('a::attr(href)').extract()

        # Gib die extrahierten Links aus
        for link in links:
            print(f'Gefundener Link: {link}')
            # self.log() ist scrapy spezifisch
            # self.log(f'Gefundener Link: {link}')