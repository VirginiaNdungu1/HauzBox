from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
# Create your tests here.
# client = APIClient()


class AccountsTest(APITestCase):

    # Originally create a user
    def setUp(self):
        self.test_user = User.objects.create_user(
            'tomnjerry', 'nishndungu8@gmail.com', 'hummingbirdcomp#')

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
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

    def test_create_user_with_short_password(self):
        '''
        Ensure user is not created for password lengths less than 8
        '''
        data = {
            'username': 'nishb',
            'email': 'ndungu.wairimu22@gmail.com',
            'password': 'abcd'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_no_password(self):
        '''
        Ensure user is not created with empty password
        '''
        data = {
            'username': 'nishb',
            'email': 'ndungu.wairimu22@gmail.com',
            'password': ''
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_long_username(self):
        '''
        Ensure user is not created with too long a username
        '''
        data = {
            'username': 'nishbernardsnishbernardsnishbernardsnishbernardsnishbernardsnishbernardsnishbernards',
            'email': 'ndungu.wairimu22@gmail.com',
            'password': 'hummingbirdcomp#'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_no_username(self):
        '''
        Ensure user is not created without a username
        '''
        data = {
            'username': '',
            'email': 'ndungu.wairimu22@gmail.com',
            'password': 'hummingbirdcomp#'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_preexisting_username(self):
        '''
        Ensure user is not created with a pre-existing username
        '''
        data = {
            'username': 'tomnjerry',
            'email': 'user@gmail.com',
            'password': 'tomnjerry'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_preexisting_email(self):
        '''
        Ensure user is not created with a pre-existing email
        '''
        data = {
            'username': 'nishb',
            'email': 'nishndungu8@gmail.com',
            'password': 'hummingbirdcomp#'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_invalid_email(self):
        '''
        Ensure user is not created with an invalid email
        '''
        data = {
            'username': 'nishb',
            'email': 'nishndungu8@',
            'password': 'hummingbirdcomp#'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_no_email(self):
        '''
        Ensure user is not created without an email
        '''
        data = {
            'username': 'nishb',
            'email': '',
            'password': 'hummingbirdcomp#'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)
