from django.contrib.auth.models import AnonymousUser
from django.shortcuts import reverse
from django.test import RequestFactory, TestCase

from ..views import home


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('home')
        self.factory = RequestFactory()

    def test_url(self):
        self.assertEqual(self.url, '/')

    def test_get(self):
        request = self.factory.get(self.url)
        request.user = AnonymousUser()

        response = home(request)
        self.assertEqual(response.status_code, 200)
