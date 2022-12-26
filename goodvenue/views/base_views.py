from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from ..models import Question
"""
 from .models import : 같은 디렉터리에 있는 models.py 모듈을 import
from ..models import 부모디렉터리의 models.py 모듈을 import
"""

# Create your base for views here. (index, detail)

#def index(request):
  # return HttpResponse("안녕하세요 ~ GoodVenue에 오신것을 환영합니다.")
  # 페이징 적용 전
   # question_list = Question.objects.order_by('-create_date')
   # context = {'question_list': question_list}

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'goodvenue/question_list.html', context)


def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id) #pk는 Question 모델의 기본키(Primary Key)에 해당 값을 의미
    context = {'question': question}
    return render(request, 'goodvenue/question_detail.html', context)
