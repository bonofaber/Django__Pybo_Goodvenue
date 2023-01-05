from django.urls import path
from articleapp.views import ArticleCreationView, ArticleDetailView, ArticleDeleteView, ArticleUpdateView, ArticleListView

app_name = 'articleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreationView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]
