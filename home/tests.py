from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeModelTestCase(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="This is a test recipe.",
            is_public=True
        )

    def test_recipe_creation(self):
        self.assertIsInstance(self.recipe, Recipe)
        self.assertEqual(self.recipe.title, "Test Recipe")
        self.assertEqual(self.recipe.description, "This is a test recipe.")
        self.assertTrue(self.recipe.is_public)

    def test_str_method(self):
        self.assertEqual(str(self.recipe), "Test Recipe")

class HomeViewTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/home.html')