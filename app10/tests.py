from django.test import TestCase, Client

# Create your tests here.
class Story10Test(TestCase):
    def test_url_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code,200)
    
    def test_inside_html(self):
        response=Client().get('')
        response_content = response.content.decode('utf-8')
        self.assertIn("Login", response_content)