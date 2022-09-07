from django.test import Client, TestCase

"""def test_home_status_code(client:Client):
    response = client.get('/')

    assert response.status_code == 200"""

def add_num(num):
    return num + 1

class SimplesTestCase(TestCase):

    def setUp(self):
        self.numero = 41

    def test_add_num(self):
        valor = add_num(self.numero)
        self.assertTrue(valor == 42)
        
