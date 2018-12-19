python manage.py runserver
python manage.py makemigrations polls 迁移
python manage.py sqlmigrate polls 0001 查看
python manage.py shell  进去
 from polls.models import Choice,Question 引入
 from django.utils import timezone 
 q=Question(question_text="下周五考",pub_date=timezone.now())
 上面插入数据
  q.save()  保存
  exit()退出
Question.objects.all()  
Question.objects.filter(id=1)
Question.objects.filter(pk=1)
Question.objects.filter(question_text__startswith='下周')
Question.objects.get(pub_date__year=timezone.now().year)

Question.objects.get(pk=1)
q = Question.objects.get(id=1)
q.was_published_recently()

 q = Question.objects.filter(question_text="下周五考")
q = Question.objects.get(id=1)
q.choice_set.create(choice_text="考试",votes=0)
q.choice_set.all()
 q.choice_set.count()

python manage.py createsuperuser




