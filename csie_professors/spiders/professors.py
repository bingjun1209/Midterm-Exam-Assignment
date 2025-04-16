import scrapy

class ProfessorsSpider(scrapy.Spider):
    name = 'professors'
    allowed_domains = ['csie.asia.edu.tw']
    start_urls = ['https://csie.asia.edu.tw/zh_tw/associate_professors_2']

    def parse(self, response):
        professors = response.css('.views-row')

        for professor in professors:
            name = professor.css('.views-field-title .field-content::text').get(default='').strip()
            expertise = professor.css('.field-name-field-professor-expertise .field-content::text').get(default='').strip()

            yield {
                '姓名': name,
                '專長領域': expertise
            }