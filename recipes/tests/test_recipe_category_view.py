from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):
    def test_recipe_category_template_dont_load_not_published_recipes(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id':recipe.category.id}))
        self.assertEqual(response.status_code, 404)   
    
    def test_recipe_category_view_functions_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
    
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)
        
    def test_recipe_category_template_loads_recipes(self):
        title_for_test ='Test Title'
        self.make_recipe(title=title_for_test)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')


        self.assertIn(title_for_test, content)
