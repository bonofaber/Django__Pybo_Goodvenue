from django.urls import path
from projectapp.views import ProjectCreationView, ProjectDetailView, ProjectDeleteView, ProjectUpdateView, ProjectListView

app_name = 'projectapp'

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'),
    path('create/', ProjectCreationView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ProjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProjectDeleteView.as_view(), name='delete'),
]
