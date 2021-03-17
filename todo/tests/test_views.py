from utils.setup_test import TestSetup
from authentication.models import User
from todo.models import Todo
from django.urls import reverse


class TestModel(TestSetup):

    def test_should_create_atodo(self):

        user = self.create_test_user()
        self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password12!'
        })

        todos = Todo.objects.all()

        self.assertEqual(todos.count(), 0)

        response = self.client.post(reverse('create-todo'), {
            'owner': user,
            'title': "Hello do this",
            'description': "Remember to do this"
        })

        updated_todos = Todo.objects.all()

        self.assertEqual(updated_todos.count(), 1)

        self.assertEqual(response.status_code, 302)
