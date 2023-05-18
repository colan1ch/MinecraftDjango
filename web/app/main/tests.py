from django.test import TestCase, Client
from django.core.exceptions import PermissionDenied
from main.models import User


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username='john',
                                        email='jlennon@beatles.com',
                                        password='glass onion')

#

    def test_index_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')

#

    def test_registration_status_code(self):
        response = self.client.get('/registration', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_registration_template(self):
        response = self.client.get('/registration', follow=True)
        self.assertTemplateUsed(response, 'registration.html')

#

    def test_servers_status_code(self):
        self.client.login(username='john', password='glass onion')
        response = self.client.get('/servers', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_servers_template(self):
        self.client.login(username='john', password='glass onion')
        response = self.client.get('/servers', follow=True)
        self.assertTemplateUsed(response, 'servers.html')

#

    def test_profile_status_code(self):
        self.client.login(username='john', password='glass onion')
        response = self.client.get('/profile', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile_template(self):
        self.client.login(username='john', password='glass onion')
        response = self.client.get('/profile', follow=True)
        self.assertTemplateUsed(response, 'profile.html')

#

    def test_login_status_code(self):
        self.client.login(username='john', password='glass onion')
        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_template(self):
        self.client.login(username='john', password='glass onion')
        response = self.client.get('/login', follow=True)
        self.assertTemplateUsed(response, 'login.html')

#

    def test_pay_status_code(self):
        self.client.login(username='john', password='glass onion')
        response = self.client.get('/api/payment/yoomoney', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_pay_template(self):
        self.client.login(username='john', password='glass onion')
        response = self.client.get('/api/payment/create_payment', follow=True)
        self.assertEqual(response.status_code, 200)

#

    def test_api_1(self):
        response = self.client.get('/api/create_server', follow=True)
        self.assertRaises(PermissionDenied)
