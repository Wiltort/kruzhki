from django.test import TestCase, Client
from django.contrib.auth.models import User


class TokenTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(
            'my_admin', 'my@ad.min', 'psss'
        )
        
    def test_page(self):
        self.client.login(
            username = self.superuser.username, 
            password = self.superuser.password)
        response = self.client.post("/api-token-auth/",)
        self.assertEqual(response.status_code, 200, 
                         msg='страница запроса "/api-token-auth/" недоступна')