from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question,Choice
from django.template import loader
from django.shortcuts import render
from  django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse #类似前端模块语言 url 函数
from django.views import generic # 从数据库取数据琴台渲染列表操作比较简单,django


# Create your views here.

# def index(request):
#     return HttpResponse("""
#         <html>
#             <head>
#             </head>
#             <body>
#                 <h1>hello world</h1>
#             </body>
#         <html>
# """)

def index(request):
    """
    展示问题列表
    :return:
    """
    question_list = Question.objects.all().order_by('-pub_date')
    # print(question_list)
    # output=''
    # for q in question_list:
    #     print(q.id,q.question_text,q.pub_date)
    #     output=output + q.question_text+','
    # print(output)
    # return HttpResponse(output)
    #output =','.join([q.question_text for q in question_list])
    template =loader.get_template('polls/index.html')
    context={
        'question_list': question_list
    }
    print(question_list)
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """
    显示一个问题的详细信息，问题内容、问题发布时间、选项内容、每个选项投票数。
    """
    try:
        question = Question.objects.get(id=question_id)
        #choices = Choice.objects.filter(question_id=question_id)
        # 由于orm代劳 question 可以直接带出相对的chonice
        # choice =question.choice_set.all()
        #  可以吧上面的带入前端
    except Question.DoesNotExist:
        raise Http404("错误")
    print(question)
    context = {
        'question': question,
        'as': '你好',
    }
    # return HttpResponse('你好')
    return render(request, 'polls/detail.html', context)


def results(request,question_id):
    """
    投票结果
    """
    question =Question.objects.all()

def vote(request,question_id):
    """
    投票结果
    """
    try:
        question = Question.objects.get(id=question_id)
        choice= question.choice_set.all()
        choice_id = request.POST['choice']
        selected_id = question.choice_set.get(id=choice_id)
    except Question.DoesNotExist as e:
        error_message='问题不存在，检查问题id'
    except Choice.DoesNotExist as e:
        error_message ='问题对应的选项不存在'
        return render(request, 'polls/detail.html', context={
           'error_message': error_message
        })
    else:
        # sql update choice set votes=votes+1 where id=2
        selected_id.votes += 1
        # commit:
        selected_id.save()
        # 投票完重定向到 views.resullts(qid)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))
# 通用模板实例  跟def index 比这看  适合适合单调的增删改查
class SimpleView(generic.ListView):
      template_name = 'polls/index.html'
      context_object_name = 'question_list'

      def get_queryset(self):
          return Question.objects.all()