#encoding: utf-8
import MySQLdb
import traceback
from MySQLdb import cursors

#导入数据
data_user = "user.data.json"
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = 'redhat'
MYSQL_DB = 'cmdb'
CHARSET = 'utf8'

def execute_mysql():
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB,
                           charset=CHARSET)
    cur = conn.cursor(cursors.DictCursor)
    print(cur)
    cur.execute()
    resutl = cur.fetchall()
    cur.close()
    conn.close()
    print(resutl)