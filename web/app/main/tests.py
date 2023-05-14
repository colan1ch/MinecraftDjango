from django.test import TestCase, Client


class Tests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_status_code(self):
        response = self.client.get('', follow=False, data=None)
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get('', follow=False, data=None)
        self.assertTemplateUsed(response, 'index.html')

    def test_servers_status_code(self):
        self.client.login(username='fedor', password='promprom')
        response = self.client.get('/servers', follow=True, data=None)
        self.assertEqual(response.status_code, 200)

    def test_servers_template(self):
        self.client.login(username='fedor', password='promprom')
        response = self.client.get('/servers', follow=True, data=None)
        self.assertTemplateUsed(response, 'servers.html')
