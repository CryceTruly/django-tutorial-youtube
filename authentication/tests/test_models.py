from utils.setup_test import TestSetup
from authentication.models import User


class TestModel(TestSetup):

    def test_should_create_user(self):

        user = self.create_test_user()

        self.assertEqual(str(user), user.email)
