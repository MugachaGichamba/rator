from django.urls import path
from . import views

urlpatterns = [
    path('new_project/', views.ProjectCreateView.as_view(), name='project-create'),
    path('my_posts/', views.my_posts, name="my-posts"),

]
