from django.urls import path

from main import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),
    path('', views.ChooseTemplateView.as_view(), name='choose'),
    path('inregistrare/', views.RegisterView.as_view(), name='signup'),
    path('profile/<int:pk>/', views.UserProfile.as_view(), name='profile'),
    path('', views.CategoryCreateView.as_view(), name='create_category'),
    path('add-job/', views.AdCreatView.as_view(), name='create_job'),
    path('list-of-jobs/', views.AdListView.as_view(), name='view_ad'),
    path('list-of-candidats/', views.UserListView.as_view(), name='list_candidates'),
    path('searched/', views.search, name='search_bar'),
    path('details/<int:pk>/', views.JobDetailsView.as_view(), name='job_details'),
    path('candidat-details/<int:pk>/', views.CandidatiiDetailsView.as_view(), name='candidate_details'),

]
