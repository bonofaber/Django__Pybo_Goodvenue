from django.contrib.auth.views import LoginView, LogoutView

from accountapp import views
#from accountapp import views
from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView
from django.urls import path, include

from django.contrib.auth import views as auth_views


app_name = 'accountapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    # header.html에서 여기  accountapp 로그인 기능 사용할 경우  (현재는 common의 login.html사용 )
   # path('login/', auth_views.LoginView.as_view(template_name='accountapp/login.html'), name='login'),
]
