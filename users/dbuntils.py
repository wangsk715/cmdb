#encoding: utf-8
import MySQLdb
import traceback
from MySQLdb import cursors

#导入数据
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = 'redhat'
MYSQL_DB = 'cmdb'
CHARSET = 'utf8'
class Conndb(object):
    @classmethod
    def execute_mysql(sql, args=(), fetch=True, one=False):
        cnt, result = 0, None
        cur, conn = None, None
        print('11',sql, 'sql_data')
        try:
            conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB,
                                   charset=CHARSET)
            cur = conn.cursor(cursors.DictCursor)
            print(cur)
            print(args)
            cnt = cur.execute(sql, args)
            print(cnt)
            if fetch:
                result = cur.fetchall() if one else cur.fetchone()
                print(result)
            else:
                conn.commit()
            cur.close()
            conn.close()
        except BaseException as e:
            print(e)
            print(traceback.format_exc())
        # finally:
        #     if cur:
        #         cur.close()
        #     if conn:
        #         conn.close()
        return cnt, result


