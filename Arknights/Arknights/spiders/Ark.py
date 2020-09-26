#FGO情人节语音爬虫
import scrapy
import re
#引入定义的item数据结构ArknightsItem
from Arknights.items import ArknightsItem 

#继承自spider类
class ArkSpider(scrapy.Spider):
    name = 'Ark' #根据这个名字执行，如果项目中有多个爬虫记得名字要唯一
    allowed_domains = ['fgo.wiki'] #域名要填对，否则后面callback无效
    start_urls = ['https://fgo.wiki/index.php?title=%E5%88%86%E7%B1%BB:%E4%BB%8E%E8%80%85%E8%AF%AD%E9%9F%B3&pagefrom=%E9%BD%90%E6%A0%BC%2F%E8%AF%AD%E9%9F%B3#mw-pages'] #一级页面第一页

    def parse(self, response):
      operator_name =  response.xpath('//div[@class="mw-category-group"][*]/ul/li[*]/a/text()').extract() #一级页面中链接名文本
      for ope_name in operator_name:
        next_url = 'http://fgo.wiki/w/{}'.format(ope_name[:-2])+'情人节剧情语音' #二级页面url名
        print(next_url)
        # yield生成请求，将新的url加入到爬取队列中，url为新的待爬取队列，callback为新的爬取调用的parse名称，这个项目新定义的为parse_item。
        yield scrapy.Request(url=next_url,callback=self.parse_item)

      global next_page   
      next_page = 'https://fgo.wiki/'+response.xpath('//div[@id="mw-pages"]//@href').extract_first() #下一页
      if next_page is not None:
        print(next_page)

    def parse_item(self, response):
       for i in range(1,3): 
         for j in range(1,61):
          item = ArknightsItem()
          item["中文文本"] = ''.join(response.xpath('//div[@class="mw-parser-output"]/table[@class="voicescripttable"][{}]/tbody/tr[{}]//p[@class="voicescript-text-cn"]//text()'.format(i,j)).extract()) #一定要注意，这里是//text()而不是/text()，否则无法识别ruby标签里的内容(xpath不识别br和ruby标签)
          item["日文文本"] = ''.join(response.xpath('//div[@class="mw-parser-output"]/table[@class="voicescripttable"][{}]/tbody/tr[{}]//p[@class="voicescript-text-jp"]//text()'.format(i,j)).extract())
          yield item
          print (item) 

       if next_page is not None:
            yield scrapy.Request(url=next_page,callback=self.parse) #第一级主页面的所有二级页面爬完后，再返回第一级主页面下一页;如果response到相同页面，爬虫会自动去除


   
