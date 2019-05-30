from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .models import Project, Rating
from django.contrib import messages


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'image', 'description', 'link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Image successfully uploaded")
        return super().form_valid(form)


class ProjectListView(ListView):
    model = Project


class RateProjectCreateView(LoginRequiredMixin, CreateView):
    model = Rating
    fields = ['content', 'design', 'usability']

    # def get_initial(self):
    #     initials = super(RateProjectCreateView, self).get_initial()
    #     project = get_object_or_404(Project, id=self.kwargs['project_id'])
    #     initials['project'] = project
    #     print(initials['project'])
    #     return initials

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.project_id =  self.kwargs['project_id']
        messages.success(self.request, "Project Rated")
        return super().form_valid(form)

