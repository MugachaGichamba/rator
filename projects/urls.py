from django.urls import path
from . import views

urlpatterns = [
    path('new_project/', views.ProjectCreateView.as_view(), name='project-create'),
    path('my_posts/', views.ProjectListView.as_view(), name="my-projects"),

]
