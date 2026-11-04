from django.test import SimpleTestCase, TestCase
from django.urls import resolve

from .models import Category
from .views import CakeCreateListCreateView, CakeRetrieveUpdateDestroyView


class CakeUrlTests(SimpleTestCase):
    def test_cake_list_url_resolves(self):
        match = resolve('/cakes/')

        self.assertIs(match.func.view_class, CakeCreateListCreateView)

    def test_cake_detail_url_resolves(self):
        match = resolve('/cakes/1/')

        self.assertIs(match.func.view_class, CakeRetrieveUpdateDestroyView)


class CategoryListTests(TestCase):
    def test_category_list_returns_existing_category_ids(self):
        category = Category.objects.create(name='Birthday cake')

        response = self.client.get('/Category/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'id': category.id, 'name': 'Birthday cake'}])
