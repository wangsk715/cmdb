#encoding: utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.models import get_users,delete_user, get_user,vaild_update_user,update_user,get_user_data,add_user,passwd
from .models import  vaild_login as valid_login_func
import time
# Create your views here.

#获取用户列表，展示用户列表
def index(request):
    if not request.session.get('user'):
        return redirect('users:login')
    return render(request, 'user/index.html',
                  {
                     'users': get_users()       }
                  )

#登录
def login(request):
    if request.method == "GET":
        return render(request, 'user/login.html')
    else:
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        user = valid_login_func(username, passwd)
        if user:
            request.session["user"] = user
            return redirect('users:index')
        else:
             return render(request, 'user/login.html',
                   {    'name': username,
                       'errors': {'default':"用户名或密码错误" }})

#退出登录
def logout(request):
    #清空session
    request.session.flush()
    return redirect('users:login')

#删除
def delete(request):
    if  not request.session.get('user'):
        return redirect('users:login')
    else:
        uid = request.GET.get('uid')
        print(uid)
        delete_user(uid)
        return redirect('users:index')

def view(request):
    if  not request.session.get('user'):
        return redirect('users:login')
    else:
        uid = request.GET.get('uid', '')
        print(uid)
        return render(request, 'user/view.html',
                        {
                            'user' : get_user(uid)
                        }
                      )


def update(request):
    if  not request.session.get('user'):
        return redirect('users:login')

    is_vaild, user, errors = vaild_update_user(request.POST)
    print(is_vaild)
    print('11',user, '1')
    if is_vaild:
        update_user(user)
        return redirect('users:index')
    else:
        return render(request, 'user/view.html',{
            'user': user,
            'errors': errors
        })

def add(request):
    #登录验证
     if not request.session.get('user'):
         return redirect('users:login')
     if request.method == "GET":
        return render(request, 'user/add.html')
     else:
         is_valid,user,errors = get_user_data(request.POST)
         print(user,'q')
         if is_valid:
             add_user(user)
             return redirect('users:index')
         else:
            return render(request, 'user/add.html',{
                'user': user,
                 'errors': errors
             })

def update_passwd(request):

    # 登录验证
    if not request.session.get('user'):
        return redirect('users:login')
    if request.method == "GET":
        return render(request, 'user/change_passwd.html')
    else:
        print(request.GET.get('uid', '1'))
        uid = request.session.get('user')['id']
        pd = request.POST.get('password', '')
        print(uid, pd, '1')
        passwd(uid, pd)
        return redirect('users:login')