import json, codecs, os, csv
from itemadapter import ItemAdapter
import uuid

id = uuid.uuid4() #生成唯一标识

# 保存为csv文件
class Pipiline_ToCSV(object):
    def __init__(self):
        #文件的位置
        store_file = os.path.dirname(__file__) + '/spiders/output_{}.csv'.format(id) #__file__表示显示文件当前的位置Arknights文件夹
        #打开文件，并设置编码
        self.file = codecs.open(filename= store_file, mode= 'wb', encoding='utf-8-sig') #这里要看一下是utf-8还是utf-8-sig，不对则会乱码

        # 写入csv
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        line = (item['中文文本'], item['日文文本']) #item元素名
        # 逐行写入     
        self.writer.writerow(line)
        return item

    def close_spider(self, spider):
        self.file.close()
        
# # 保存为json文件
# class JsonPipeline(object):
#     def __init__(self):
#         #文件的位置
#         store_file = os.path.dirname(__file__) + '/spiders/output.json'
#         # 打开文件，设置编码为utf-8
#         self.file = codecs.open(filename= store_file, mode= 'wb', encoding='utf-8-sig')

#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) +',\n'
#         # 逐行写入
#         self.file.write(line)
#         return item

#     def close_spider(self, spider):
#         self.file.close()

