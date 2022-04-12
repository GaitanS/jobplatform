from datetime import datetime, timedelta

from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count

from main.form import UserForm, UserEditForm
from main.models import User, Category, Ad


def common_data(request):
    all_candidates = User.objects.filter(is_superuser=0)
    all_ads = Ad.objects.all().order_by('-created_at')
    all_jobs = Ad.objects.all().count()
    all_jobs_in_the_past_7_days = Ad.objects.filter(created_at__gte=datetime.now() - timedelta(days=7))
    profile = None
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
    context = {'user_form': UserForm(),
               'login_form': AuthenticationForm(),
               'profil': profile,
               'all_ads': all_ads,
               'all_candidates': all_candidates,
               'all_jobs': all_jobs,
               'all_jobs_in_the_past_7_days': all_jobs_in_the_past_7_days.count(),
               }
    return context
