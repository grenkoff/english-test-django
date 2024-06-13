from django.urls import path
from .views import (
    HomePageView,
    QuizPageView,
    custom_logout_view,
)

urlpatterns = [
    path("logout/", custom_logout_view, name='logout'),
    path("quiz/", QuizPageView.as_view(), name="quiz"),
    path("", HomePageView.as_view(), name="home"),
]
