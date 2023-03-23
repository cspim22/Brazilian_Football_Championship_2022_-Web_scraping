import scrapy

class FutebolSpider(scrapy.Spider):
    
    # Habilitação
    name= 'bot' 

    # request
    def start_requests(self):
        urls = ['https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022;']

        for url in urls:
            yield scrapy.Request(url = url, callback= self.parse)

    # response

    def parse(self, response):
        
        time_xpath = response.xpath("//span[@class='hidden-xs']//text()")
        pontos_xpath = response.xpath("//th[@scope='row']//text()")
        vitorias_xpath = response.xpath("//tr[@class='expand-trigger']//td[3]//text()")


        for times, pontos, vitorias in zip(time_xpath, pontos_xpath, vitorias_xpath):
            yield {
                'time': times.get(),
                'pontos': pontos.get(),
                'vitorias' : vitorias.get()
            }
    