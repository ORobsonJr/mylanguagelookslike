from django.test import TestCase
from django.urls import reverse
from .models import User

class FindUserByUsernameViewTest(TestCase):
    def setUp(self):
        # Create a test user for the test database
        self.user = User.objects.create(username='testuser', 
                                        full_name = '',
                                        email='testuser@example.com',
                                        password='pass123',
                                        )

    def test_find_user_by_username(self):
        # Use reverse to get the URL for the view
        url = reverse('find_user_by_username')

        # Make a GET request to the view with a valid username
        response = self.client.get(url, {'username': 'testuser'})

        # Check that the response status code is 200 (OK)
        #self.assertEqual(response.status_code, 200)

        # Check that the returned user is the one we expect
        #self.assertEqual(response.context['user'].username, 'testuser')

