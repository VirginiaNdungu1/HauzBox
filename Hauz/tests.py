from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
# Create your tests here.
client = APIClient()


class AccountsTest(APITestCase):

    # Originally create a user
    def setUp(self):
        self.test_user = User.objects.create_user(
            'testuser', 'nishndungu8@gmail.com', 'hummingbirdcomp#')

        # URL for creating a user Account
        self.create_url = reverse('account-create')

    def test_create_user(self):
        '''
        Ensure new user is created and a valid token is created with it
        '''
        data = {
            'username': 'nishb',
            'email': 'ndungu.wairimu22@gmail.com',
            'password': 'hummingbirdcomp#'
        }

        response = self.client.post(self.create_url, data, format='json')
        # make sure the db has two users
        self.assertEqual(User.objects.count(), 2)
        # make sure we return a 201 created code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # return the user attributes upon successful creation
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)
