#encoding: utf-8
import json
from django.db import models
import MySQLdb
from MySQLdb import cursors
# Create your models here.

#导入数据
data_user = "user.data.json"
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = 'redhat'
MYSQL_DB = 'cmdb'
CHARSET = 'utf8'
# conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='redhat', db='cmdb',charset='utf8')
# daya_user = conn.cursor()
sql_login = "select id,name,age,sex,tel from users where name=%s and password=%s limit 1;"
sql_list = '''
            select id,name,sex,age,tel
            from users;
            '''
sql_delete = '''
                delete from users where id=%s;
            '''
sql_update = '''
            select id,name,sex,age,tel
            from users
            where id=%s;
    '''
sql_update_vaild = '''
                 update users 
                 set name=%s,sex=%s,age=%s,tel=%s 
                 where id=%s
                    '''
user_modle = "{'id': line[0], 'name':line[1], 'sex':line[2], 'age':line[3], 'tel':line[4]}"
mysql_colume = {'id', 'name', 'age', 'sex', 'tel'}
sql_insert = '''
            insert into users(name, sex, age, tel, password)
            values (%s, %s, %s, %s, %s);
            '''
sql_passwd = '''
            update users
            set password=%s
            where id=%s;
            '''
def get_users():
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB, charset=CHARSET)
    cur = conn.cursor(cursors.DictCursor)
    print(cur)
    cur.execute(sql_list)
    resutl = cur.fetchall()
    print(resutl)
    cur.close()
    conn.close()
    print(resutl)
    return resutl

def get_user(uid):
    uid = int(uid)
    print(type(uid))
    print(uid)
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB,
                           charset=CHARSET)
    cur = conn.cursor(cursors.DictCursor)
    print(cur)
    cur.execute(sql_update, (uid,))
    resutl = cur.fetchone()
    print(resutl)
    cur.close()
    conn.close()
    return resutl

def users_dump(users):
    with open(data_user, 'wt') as f:
        f.write(json.dumps(users))
    return True



def vaild_login(username, passwd):
    conn = MySQLdb.connect(host= MYSQL_HOST, port = MYSQL_PORT, user = MYSQL_USER, passwd = MYSQL_PASSWD, db = MYSQL_DB, charset = CHARSET)
    print("查询成功")
    cur = conn.cursor()
    print(cur)
    print('test')
    cur.execute(sql_login,(username, passwd))
    resutl = cur.fetchone()
    cur.close()
    conn.close()
    return {"id": resutl[0], 'name': resutl[1]}  if resutl else None

def delete_user(uid):
    uid = int(uid)
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB,charset=CHARSET)
    print("查询成功")
    cur = conn.cursor()
    print(cur)
    print('test')
    cur.execute(sql_delete, (uid,))
    conn.commit()
    cur.close()
    conn.close()

    return True

def vaild_update_user(params):
    uid = params.get('id', '')
    name = params.get('name', '')
    age = params.get('age', '')
    sex = params.get('sex', '')
    tel = params.get('tel', '')

    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB,
                           charset=CHARSET)
    cur = conn.cursor(cursors.DictCursor)
    cur.execute(sql_update, (uid))
    users = cur.fetchone()
    cur.close()
    conn.close()
    users_info = users
    print(users_info)

    is_valid = True
    user = {}  #{id,name,age,sex,tel}
    errors = {}

    #判断用户id是否存在
    user['id'] = uid.strip()
    if users_info.get('id') is None:
        errors['id'] = '输入用户信息不存在'
        is_valid = False

    user['name'] = name
    if users_info['name'] == user['name'] and users_info['id'] != int(user['id']):
        errors['name'] = "用户名存在"
        is_valid = False

    user['age'] = age
    if not user['age'].isdigit():
        errors['age'] = "年龄格式错误"
        is_valid = False

    user['tel'] = tel
    if not user['tel'].isdigit():
        errors['tel'] = '电话格式错误'
        is_valid  = False

    user['sex']  = sex

    print(user)

    return is_valid, user, errors


def update_user(user):
    uid = user['id']
    name = user['name']
    age = user['age']
    sex = user['sex']
    tel = user['tel']

    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB,
                           charset=CHARSET)
    print("查询成功")
    cur = conn.cursor()
    print(cur)
    print('test')
    cur.execute(sql_update_vaild, (name, sex, age, tel, uid))
    conn.commit()
    cur.close()
    conn.close()

    return True

def get_user_data(params):
    name = params.get('name', '')
    age = params.get('age', '')
    sex = params.get('sex', '')
    tel = params.get('tel', '')
    password = params.get('password', '')
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB,
                           charset=CHARSET)
    cur = conn.cursor(cursors.DictCursor)
    cur.execute(sql_list)
    users = cur.fetchall()
    cur.close()
    conn.close()
    users = users

    is_valid = True
    user = {}  # {id,name,age,sex,tel}
    errors = {}
    for users_info in users:
        user['name'] = name
        if users_info['name'] == user['name'] and users_info['id'] != int(user['id']):
            errors['name'] = "用户名存在"
            is_valid = False

        user['age'] = age
        if not user['age'].isdigit():
            errors['age'] = "年龄格式错误"
            is_valid = False

        user['tel'] = tel
        if not user['tel'].isdigit():
            errors['tel'] = '电话格式错误'
            is_valid = False

        user['sex'] = sex
        user['password'] = password
    print(user,'1')

    return is_valid, user, errors


def add_user(user):
    name = user['name']
    age = int(user['age'])
    sex = user['sex']
    tel = user['tel']
    password = user['password']

    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB,
                           charset=CHARSET)
    cur = conn.cursor()
    cur.execute(sql_insert, (name, sex, age, tel, password))
    conn.commit()
    cur.close()
    conn.close()
    return True

def passwd(uid, pd):
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB,
                          charset=CHARSET)
    cur = conn.cursor(cursors.DictCursor)
    cur.execute(sql_passwd, (pd, uid))
    conn.commit()
    cur.close()
    conn.close()

    return True
if __name__ == '__main__':
    get_user()