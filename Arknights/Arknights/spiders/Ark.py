import scrapy
#引入定义的item数据结构ArknightsItem
from Arknights.items import ArknightsItem 

#继承自spider类
class ArkSpider(scrapy.Spider):
    name = 'Ark' #根据这个名字执行，如果项目中有多个爬虫记得名字要唯一
    allowed_domains = ['prts.wiki'] #域名要填对，否则后面callback无效
    start_urls = ['http://prts.wiki/w/%E5%88%86%E7%B1%BB:%E5%B9%B2%E5%91%98%E8%AF%AD%E9%9F%B3'] #一级页面

    def parse(self, response):
      operator_name =  response.xpath('//div[@class="mw-category-group"][*]//li[*]/a/text()').extract() 
      for ope_name in operator_name:
        next_url = 'http://prts.wiki/w/{}'.format(ope_name)
        print(next_url)
        # yield生成请求，将新的url加入到爬取队列中，url为新的待爬取队列，callback为新的爬取调用的parse名称，这个项目新定义的为parse_item。
        yield scrapy.Request(url=next_url,callback=self.parse_item)   

    def parse_item(self, response):
       for i in range(1,36): #每位干员最多35组台词
        item = ArknightsItem()
        item["中文文本"] = response.xpath('//table[@class="wikitable nomobile"]/tbody/tr[{}]//p[2]/text()'.format(i)).extract_first() #[0]表示只提取里面的元素，为空时会报错，用first()更好
        item["日文文本"] = response.xpath('//table[@class="wikitable nomobile"]/tbody/tr[{}]//p[1]/text()'.format(i)).extract_first()
        yield item
        print (item) 

        # yield scrapy.Request(url=next_url,callback=self.parse_item)  
        #获取下一页的连接
        #next_page = response.xpath('//*[@id="content"]/div[3]/div[3]/div/div[2]/a[11]/@href').get()
        # 如果有下一页跳到下一页继续爬取
        # if next_page is not None:
            # yield response.follow(next_page, self.parse)