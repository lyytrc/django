from django.urls import path

from . import  views

urlpatterns=[
   path('',views.index,name='index'),
path('index',views.index,name='index'),
]

#先引入视图函数
# path()函数定义的路由都会在项目启动时候加载
#path路由规则