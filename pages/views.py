from django.views.generic import TemplateView, ListView
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Quiz


class HomePageView(TemplateView):
    template_name = "home.html"


class QuizPageView(ListView):
    model = Quiz
    template_name = "quiz.html"


def custom_logout_view(request):
    logout(request)
    return redirect("home")
