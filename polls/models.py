from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('问题内容',max_length=200)
    pub_date = models.DateTimeField('发布时间')


class Choice(models.Model):
    question = models.ForeignKey(Question,  on_delete=models.CASCADE)
    choice_text=models.CharField('选项内容',max_length=200)
    votes = models.IntegerField('投票数',default=0)


"""
类被翻译成sql执行
create table question if not exits(
      id int primary key increase,
      question_text char(200) commit "问题内容"，
      pub_data datetime comment "发布时间"
）
"""
# django自带orm框架，用法类似于sqlalchemy
# 自定义的类要继承orm框架中的model类，这样orm就可以吧类和数据库关联到一块

