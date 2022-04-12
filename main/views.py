import operator
from functools import reduce

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView

from main.form import UserForm, CategoryForm, AdForm, UserEditForm
from main.models import User, Category, Ad


class HomeTemplateView(TemplateView):
    template_name = 'homepage/homepage.html'


class ChooseTemplateView(TemplateView):
    template_name = 'choose.html'


class JobDetailsView(DetailView):
    template_name = 'job_details.html'
    model = Ad


class CandidatiiDetailsView(DetailView):
    template_name = 'user_details.html'
    model = User


# User register, profile and list
class RegisterView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('homepage')


class UserProfile(UpdateView):
    template_name = 'registration/profil.html'
    model = User
    context_object_name = 'user_profil'
    form_class = UserEditForm
    success_url = reverse_lazy('homepage')


class UserListView(ListView):
    template_name = 'userextend/user_list.html'
    model = User
    permission_required = 'ad.view_candidates'


# Ad create and list
class AdCreatView(LoginRequiredMixin, CreateView):
    template_name = 'add_new_job.html'
    model = Ad
    form_class = AdForm
    success_url = reverse_lazy('homepage')


class AdListView(ListView):
    template_name = 'job_list.html'
    model = Ad
    permission_required = 'ad.view_ad'


# Category create and list
class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('homepage')
    permission_required = 'category.add_category'


def search(request):
    query = request.POST.get('q', '')
    query = query.split(' ')
    x = Ad.objects.filter(reduce(operator.and_, (Q(name__icontains=w) for w in query)))
    return render(request, 'search_job.html', {'searched': x})
