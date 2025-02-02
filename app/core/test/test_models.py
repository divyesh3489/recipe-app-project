from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''
        email = 'test@gmail.com'
        password='Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        emails = [
            ['test1@GMAIL.com','test1@gmail.com'],
            ['test2@Gmail.com','test2@gmail.com'],
            ['test3@GMAIL.COM','test3@gmail.com'],
            ['test4@gmail.COM','test4@gmail.com'],
        ]
        for email,excpected in emails:
            user = get_user_model().objects.create_user(email,'Testpass123')
            self.assertEqual(user.email,excpected)

    def test_new_user_with_out_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','Testpass123')

    def test_new_user_with_out_password(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('test4@gmail.com','')
    
    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser("test@gmail.com",'Test@123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)