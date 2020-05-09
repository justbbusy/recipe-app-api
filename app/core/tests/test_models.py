from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_case_with_email_successful(self):
        """ test to create user with email and pwd"""
        email = 'test@test.com'
        password = 'pass#test'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertTrue(user.check_password(password))

    def test_case_with_email_normalized(self):
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='password'
        )

        self.assertEqual(user.email, email.lower())

    def test_case_with_no_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password')

    def test_case_with_superuser(self):
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_superuser(
            email=email,
            password='password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
