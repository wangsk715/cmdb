#encodig: utf-8
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
            path('index/', views.index, name='index' ),
            path('login/', views.login, name='login'),
            path('logout/', views.logout, name='logout'),
            path('delete/',views.delete, name='delete'),
            path('view/', views.view, name='view'),
            path('update/', views.update, name='update'),
            path('add/', views.add, name='add'),
            path('update_passwd/', views.update_passwd, name='update_passwd'),
]

