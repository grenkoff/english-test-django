from django.urls import path

from . import views

app_name = 'quiz'

urlpatterns = [
    # question views
    path('', views.question_list, name='quiz'),
    path('results/', views.results, name='results'),
]
