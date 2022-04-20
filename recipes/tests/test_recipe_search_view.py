from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeSearchViewTest(RecipeTestBase):   
    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)
    
    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search')+ '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
    
    def test_recipe_search_raises_404_if_search_is_empty(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        response = self.client.get(reverse('recipes:search')+ '?q=<Teste>')
        self.assertIn(
            'Search for &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )

    def test_recipe_search_is_able_to_find_recipe_by_title(self):
        title1 = 'recipe1'
        title2 = 'recipe2'

        recipe1 = self.make_recipe(
            slug='one', title=title1, author_d = {'username':'one'}
        )
        
        recipe2 = self.make_recipe(
            slug='two', title=title2, author_d = {'username':'two'}
        )
    
        url = reverse('recipes:search')
        response1 = self.client.get((f'{url}?q={title1}'))
        response2 = self.client.get((f'{url}?q={title2}'))
        responseBoth = self.client.get((f'{url}?q=recipe'))

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, responseBoth.context['recipes'])
        self.assertIn(recipe2, responseBoth.context['recipes'])
    


    
