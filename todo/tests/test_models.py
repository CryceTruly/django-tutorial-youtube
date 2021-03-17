from utils.setup_test import TestSetup
from authentication.models import User
from todo.models import Todo


class TestModel(TestSetup):

    def test_should_create_user(self):
        user = self.create_test_user()
        todo = Todo(owner=user, title="Buy milk", description='get it done')
        todo.save()
        self.assertEqual(str(todo), 'Buy milk')
