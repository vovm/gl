# add a minimal pool of tests for the next code:
# rewrite this code if you have a better variant
import unittest
 
ADMIN_USER = "vasja.pupkin"
ADMIN_PASSWD = "passsecret"


def valid_admin_user(username, password):
    return username.lower().strip() == ADMIN_USER and password.strip() == ADMIN_PASSWD


class TestAdminUser(unittest.TestCase):

    def test_invalid_username(self):
        self.assertFalse(valid_admin_user("ivan", ADMIN_PASSWD))

    def test_invalid_password(self):
        self.assertFalse(valid_admin_user(ADMIN_USER, "123"))

    def test_invalid_username_and_password(self):
        self.assertFalse(valid_admin_user("ivan", "123"))

    def test_valid_const(self):
        self.assertTrue(valid_admin_user(ADMIN_USER, ADMIN_PASSWD))

    def test_check_uppercase_username(self):
        self.assertTrue(valid_admin_user("Vasja.Pupkin", ADMIN_PASSWD))

    def test_check_username_with_space(self):
        self.assertTrue(valid_admin_user(" vasja.pupkin ", ADMIN_PASSWD))

    def test_check_password_with_space(self):
        self.assertTrue(valid_admin_user(ADMIN_USER, "passsecret "))

    def test_without_one_argument(self):
        with self.assertRaises(TypeError):
            valid_admin_user(ADMIN_USER)

    def test_without_arguments(self):
        with self.assertRaises(TypeError):
            valid_admin_user()

    def test_with_another_types(self):
        with self.assertRaises(AttributeError):
            valid_admin_user(2, [0, 5])


if __name__ == '__main__':
    unittest.main()
