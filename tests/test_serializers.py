from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import Client


class TestToto(TestCase):

    def setUp(self):
        self.client = Client()

    def test_ok(self):
        response = self.client.get('/items?param=1')
        self.assertEqual(response.status_code, 200)

    def test_bad_request(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 400)

    def test_not_found(self):
        response = self.client.get('/not-items')
        self.assertEqual(response.status_code, 404)
        self.assertDictEqual(response.data, {'error': 'Not found'})

    def test_forbidden(self):
        response = self.client.get('/forbidden-items')
        self.assertEqual(response.status_code, 403)
        self.assertDictEqual(response.data, {'error': 'Permission denied'})
