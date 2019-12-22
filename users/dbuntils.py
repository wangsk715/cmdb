#encoding: utf-8
import MySQLdb
import traceback
from MySQLdb import cursors
from django.db import connection
class Conndb(object):
    @classmethod
    def execute_mysql(cls,sql, args=(), fetch=True, one=False):
        cnt, result = 0, None
        cur, conn = None, None
        print('11',sql, 'sql_data')
        try:
            cur = connection.cursor()
            print(dir(connection))
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
        except BaseException as e:
            print(e)
            print(traceback.format_exc())
        # finally:
        #     if cur:
        #         cur.close()
        #     if conn:
        #         conn.close()
        return cnt, result


