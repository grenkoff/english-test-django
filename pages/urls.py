from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('logout/', views.custom_logout_view, name='logout'),
    # path("quiz/", QuizPageView.as_view(), name="quiz"),
    path('', views.home_page, name='home'),
]
