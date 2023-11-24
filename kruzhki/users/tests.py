from django.test import TestCase, Client
from django.contrib.auth.models import User


class TokenTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(
            'my_admin', 'my@ad.min', 'psss'
        )
        self.teacheruser = User.objects.create_user(
            username='Makar', email='ma@ka.ru', password='maka', 
            is_staff = True
        )
        self.studuser = User.objects.create_user(
            username='Luk', email='ta@tu.in', password='force'
        )
        
    def test_page(self):
        data = {"username": "my_admin", "password": "psss"}
        response = self.client.post("/api-token-auth/", data=data)
        self.assertEqual(response.status_code, 200, 
                         msg='страница запроса "/api-token-auth/" недоступна')
        Token = response.json()["token"] 
        res = self.client.get('/api/v1/users/')
        self.assertEqual(res.status_code, 401, 
                         msg = 'Неавторизованный доступ к странице юзеров')
        data = {"Authorization": f"Token {Token}"}
        res = self.client.get('/api/v1/users/', headers = data)
        self.assertEqual(
            res.status_code, 200, 
            msg = 'У авторизованного юзера нет доступа к странице юзеров'
        )