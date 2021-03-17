from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from utils.setup_test import TestSetup


class TestViews(TestSetup):

    def test_should_show_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")

    def test_should_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")

    def test_should_signup_user(self):
        response = self.client.post(reverse("register"), self.user)
        self.assertEquals(response.status_code, 302)

    def test_should_not_signup_user_with_taken_username(self):

        self.user = {
            "username": "username",
            "email": "email@hmail2.com",
            "password": "password",
            "password2": "password"
        }

        self.client.post(reverse("register"), self.user)
        response = self.client.post(reverse("register"), self.user)
        self.assertEquals(response.status_code, 409)

        storage = get_messages(response.wsgi_request)

        self.assertIn("Username is taken, choose another one",
                      list(map(lambda x: x.message, storage)))

    def test_should_not_signup_user_with_taken_email(self):

        self.user = {
            "username": "username1",
            "email": "email@hmail2.com",
            "password": "password",
            "password2": "password"
        }

        self.test_user2 = {
            "username": "username11",
            "email": "email@hmail2.com",
            "password": "password",
            "password2": "password"
        }

        self.client.post(reverse("register"), self.user)
        response = self.client.post(reverse("register"), self.test_user2)
        self.assertEquals(response.status_code, 409)

    def test_should_login_successfully(self):
        user = self.create_test_user()
        response = self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password12!'
        })
        self.assertEquals(response.status_code, 302)

        storage = get_messages(response.wsgi_request)

        self.assertIn(f"Welcome {user.username}",
                      list(map(lambda x: x.message, storage)))

    def test_should_not_login_with_invalid_password(self):
        user = self.create_test_user()
        response = self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password12!32'
        })
        self.assertEquals(response.status_code, 401)

        storage = get_messages(response.wsgi_request)

        self.assertIn("Invalid credentials, try again",
                      list(map(lambda x: x.message, storage)))
