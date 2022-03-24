import pymysql

# 连接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='ss99bu88',
                             database='民宿客房管理系统',
                             charset='utf8')
cursor = connection.cursor()  # 创建游标
