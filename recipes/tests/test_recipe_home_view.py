from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):


    def test_recipe_home_view_functions_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    
    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_home_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
    
    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes available', response.content.decode('utf-8'))
    
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn('Recipe Title', content)
    
    def test_recipe_home_template_dont_load_not_published_recipes(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('<h1>No recipes available</h1>', response.content.decode('utf-8'))

    
    def test_recipe_home_template_loads_published_recipes(self):
        title_for_test ='Test Title'
        self.make_recipe(is_published=True, title=title_for_test)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(title_for_test, response.content.decode('utf-8'))
    

    
