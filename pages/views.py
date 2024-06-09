from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class TestPageView(TemplateView):
    template_name = "test.html"
