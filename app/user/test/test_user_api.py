from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
def create_user(**params):    
    return get_user_model().objects.create_user(**params)

class PublicuserAPTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()

    
    def test_create_user_success(self):
        payload = {
            "email":"test@gmail.com",
            "password":"test@123",
            "name":'test'
        }
        res = self.client.post(CREATE_USER_URL,payload)
        
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        print(payload['password'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password',res.data)
        
    def test_create_user_email_exists_error(self):
        
        payload = {
            "email":"test@gmail.com",
            "password":"test@123",
            "name":'test'
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL,payload)
        
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        
    def test_create_user_password_short_error(self):
        
        payload = {
            "email":"test@gmail.com",
            "password":"test",
            "name":'test'
        }
        res = self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email = payload['email']).exists()
        self.assertFalse(user_exists)        
        
    def test_cerate_token_for_user(self):
        user_create = {
            "email":"test@gmail.com",
            "password":"test@123",
            "name":'test'
        }
        create_user(**user_create)
        payload = {
            "email":"test@gmail.com",
            "password":"test@123"
        }
        
        res = self.client.post(TOKEN_URL,payload)
        self.assertIn('token',res.data)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        
    def test_cerate_token_bad_credentials(self):
        user_create = {
            "email":"test@gmail.com",
            "password":"test@123",
            "name":'test'
        }
        create_user(**user_create)
        payload = {
            "email":"test@gmail.com",
            "password":"test@12"
        }
        res = self.client.post(TOKEN_URL,payload)
        self.assertNotIn('token',res.data)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
    
        
        
        
        
        
        
        