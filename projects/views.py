from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  CreateView
from .models import Project
from django.contrib import messages


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'image', 'description', 'link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Image successfully uploaded")
        return super().form_valid(form)

