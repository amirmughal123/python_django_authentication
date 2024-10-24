from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):


    def test_create_test_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testexample123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_test_user_normalize_email_successful(self):
        test_emails = [
            ['test1@EXample.com', 'test1@example.com'],
            ['test2@EXAMPLE.com', 'test2@example.com'],
        ]

        for email, expected in test_emails:
            user = get_user_model().objects.create_user(
                email = email,
                password = 'sample123',
            )

            self.assertEqual(user.email, expected)

    def test_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')


    def test_super_user_successful(self):
        email = 'superuser@example.com'
        user = get_user_model().objects.create_superuser(
            email = 'superuser@example.com',
            password = 'superuserexample123'
        )

        self.assertTrue(user.email, email)
        self.assertTrue(user.is_superuser, True)
        self.assertTrue(user.is_staff)
