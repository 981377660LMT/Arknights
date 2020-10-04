import json, codecs, os, csv
from itemadapter import ItemAdapter
import uuid
import pymysql

class ArkSpiderPipeline(object):
    def __init__(self):
        # 1. 建立数据库的连接
        self.connect = pymysql.connect(
	    # 连接的是本地数据库
            host='192.168.5.128',
            # mysql数据库的端口号
            port=3306,
            # 数据库的用户名
            user='root',
            # 本地数据库密码
            passwd='a2818088',
            # 数据库名
            db='FGO',
            # 编码格式
            charset='utf8'
        )
        # 2. 创建一个游标cursor, 是用来操作表。
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 3. 将Item数据放入数据库，默认是同步写入。
        insert_sql = "INSERT INTO FGO(中文文本,日文文本) VALUES ('%s', '%s')" % (item['中文文本'], item['日文文本']) #FGO是表名
        self.cursor.execute(insert_sql)

        # 4. 提交操作
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()












'''id = uuid.uuid4() #生成唯一标识

# 保存为csv文件
class Pipiline_ToCSV(object):
    def __init__(self):
        #文件的位置
        store_file = os.path.dirname(__file__) + '/spiders/outputFGO_{}.csv'.format(id) #__file__表示显示文件当前的位置Arknights文件夹
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
        self.file.close()'''
        
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

