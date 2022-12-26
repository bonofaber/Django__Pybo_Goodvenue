from django.urls import path
from . import views

from .views import base_views, question_views, answer_views


app_name = 'goodvenue'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),    # '' 사용 이유: config/urls.py 에서 이미 goodvenue/로 시작하는 URL이 goodvenue/urls.py로 이미 매핑되었기 때문
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    #추천
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
]