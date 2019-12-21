#encoding: utf-8
import json
from django.db import models
import MySQLdb
from MySQLdb import cursors
# Create your models here.
import hashlib
from users.dbuntils import Conndb

print('test')
# conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='redhat', db='cmdb',charset='utf8')
# daya_user = conn.cursor()
sql_login = '''select id,name,age,sex,tel from users where name=%s and password=%s limit 1;'''
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
    cnt,result = Conndb.execute_mysql(sql_list,{},True,True)
    return result

def get_user(uid):

    cnt,result = Conndb.execute_mysql(sql_update, (uid, ))
    return result


def vaild_login(username, passwd):
    md5 = hashlib.md5()
    md5.update(passwd.encode('utf-8'))
    passwd = md5.hexdigest()
    print(sql_login)
    args = (username, passwd)
    cnt,resutl = Conndb.execute_mysql(sql_login, args)
    print(resutl,'11')
    return {"id": resutl['id'], 'name': resutl['name']}  if resutl else None

def delete_user(uid):
    uid = int(uid)
    cnt,restult = Conndb.execute_mysql(sql_delete, (uid,), False)
    return True

def vaild_update_user(params):
    uid = params.get('id', '')
    name = params.get('name', '')
    age = params.get('age', '')
    sex = params.get('sex', '')
    tel = params.get('tel', '')

    cnt,users = Conndb.execute_mysql(sql_list,{}, True, True)
    is_valid = True
    user = {}  #{id,name,age,sex,tel}
    errors = {}
    for users_info in users:
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
    args = (name, sex, age, tel, uid)
    cnt, result = Conndb.execute_mysql(sql_update_vaild, args, True, True)
    return True

def get_user_data(params):
    name = params.get('name', '')
    age = params.get('age', '')
    sex = params.get('sex', '')
    tel = params.get('tel', '')
    password = params.get('password', '')

    cnt,users = Conndb.execute_mysql(sql_list, '', True, True)
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

    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    password = md5.hexdigest()
    agrs = (name, sex, age, tel, password)
    cnt,users = Conndb.execute_mysql(sql_insert, agrs, False)
    return True


def passwd(uid, pd):
    md5 = hashlib.md5()
    md5.update(pd.encode('utf-8'))
    pd = md5.hexdigest()
    agrs = (pd, uid)
    cnt, users = Conndb.execute_mysql(sql_passwd, agrs, False)
    return True

if __name__ == '__main__':
    get_user()