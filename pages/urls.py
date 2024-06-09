from django.urls import path
from .views import HomePageView, QuizPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("quiz/", QuizPageView.as_view(), name="quiz"),
]
