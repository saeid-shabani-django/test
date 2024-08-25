from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_by_url(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code,200)

    def test_home_page_word(self):
        res = self.client.get(reverse('home'))
        self.assertContains(res,'Home Page')

    def test_home_page_template_use(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'home.html')