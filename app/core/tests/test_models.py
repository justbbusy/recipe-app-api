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

        self.assertEqual(user.email, email)

        self.assertTrue(user.check_password(password))
