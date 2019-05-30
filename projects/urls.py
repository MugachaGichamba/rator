from django.urls import path
from . import views

urlpatterns = [
    path('new_project/', views.ProjectCreateView.as_view(), name='project-create'),
    path('my_posts/', views.ProjectListView.as_view(), name="my-projects"),
    # path('rate_post/(?P<class>\d+)/$', CreateSessionsView.as_view(), name='create_sessions')
    path('rate_project/<int:project_id>/', views.RateProjectCreateView.as_view(), name='rate_project'),

]
