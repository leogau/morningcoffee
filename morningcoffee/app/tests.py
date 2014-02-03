from django.test import TestCase
from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve
from views import index

class AppTests(TestCase):
	def test_root_resolves_to_main_view(self):
		main_page = resolve('/')
		self.assertEqual(main_page.func, index)

	def test_returns_appropriate_html(self):
		index = self.client.get('/')
		self.assertEquals(index.status_code, 200)

	def test_uses_index_html_template(self):
		index = self.client.get('/')
		self.assertTemplateUsed(index, 'index.html')

