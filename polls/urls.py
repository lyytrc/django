from django.urls import path

from . import views

app_name='polls'
urlpatterns=[
   # 首页 http://ip:port/polls/
   path('',views.index,name='index'),
   # 首页 问题列表 polls/index/
   path('index',views.index,name='index'),
   # 问题详情页 ex:// polls/1
   path('<int:question_id>/',views.detail,name='detail'),
   # 投票结果页  poll2/results
   path('<int:question_id>/results',views.results,name='results'),
   # 去投票 选项计数加一   /polls/5/vote
   path('<int:question_id>/vote', views.vote, name='vote'),

   path('simple/',views.SimpleView.as_view,name='simple')
]
# (注意)djangol.x 路由方法是  正则风格   以前的写法
# from django.conf.urls import url
# urlpatterns=[
#     # /polls/
#    url(r'^$',views.index,name='index'),
#     # index
#    url(r'^index$',views.index),
#    # /polls/5
#    url(r'^(?P<question_id>[0-9]+)/#'),
# ]


#先引入视图函数
# path()函数定义的路由都会在项目启动时候加载
#path路由规则