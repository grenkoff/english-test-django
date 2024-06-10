from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import Quiz


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Home page</h1>")


class QuizPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.quiz = Quiz.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.quiz.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/quiz/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("quiz"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quiz.html")
        self.assertContains(response, "This is a test!")
