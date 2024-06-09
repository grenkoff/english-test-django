from django.views.generic import TemplateView, ListView
from .models import Quiz

class HomePageView(TemplateView):
    template_name = "home.html"


class QuizPageView(ListView):
    model = Quiz
    template_name = "quiz.html"
