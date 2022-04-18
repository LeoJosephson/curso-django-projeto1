from django.contrib.auth.models import User
from django.test import TestCase
from recipes.models import Category, Recipe

class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)
    
    def make_author(self, 
        first_name = 'user',
        last_name='name',
        username='username',
        password='1234',
        email='user@gmail.com',):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )
    def make_recipe(self,
            category_d=None,
            author_d=None,
            title = 'Recipe Title',
            description = 'Recipe Description',
            slug = 'recipe-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Porções',
            preparation_steps = 'Recipe Preparation Steps',
            preparation_steps_is_html = False,
            is_published = True,):

        if category_d is None:
            category_d = {}
        
        if author_d is None:
            author_d = {}
        return Recipe.objects.create(
            category=self.make_category(**category_d),
            author=self.make_author(**author_d),
            title = title,
            description = description,
            slug = slug,
            preparation_time =preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published,
        )
        
    