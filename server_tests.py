import unittest
from server import app
import photo_spots
import model


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        """Perform these items before every test."""

        model.connect_to_db(app, "postgresql:///testdb")

        model.db.create_all()
        model.example_data()

    def tearDown(self):
        """Do at end of every test."""

        model.db.session.close()
        model.db.drop_all()

    def test_register_user(self):
        user_info = {'fname': 'Jamie', 'password': 'happy33',
                     'lname': 'Nelson', 'email': 'jnelson@gmail.com'}

        assert photo_spots.register_user(user_info)


class FunctionalTests(unittest.TestCase):

    def test_user_exists(self):
        assert photo_spots.user_exists('<User user_id=1 email=bcruz@gmail.com>') is True


class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Perform these items before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        """Test homepage URL path."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn('<h1>Photo Spots</h1>', result.data)

    def test_user_login(self):
        """Test user login path."""

        result = self.client.get("/user-login")

        self.assertEqual(result.status_code, 200)
        self.assertIn('<h1>User Login</h1>', result.data)


    # def test_search_results(self):
    #     """Test search result URL path."""

    #     result = self.client.get("/search-results")
    #     self.assertEqual(result.status_code, 200)

    # def test_photo_details(self):
    #     """Test photo details URL path."""

    #     result = self.client.get("/photo-details/<photo_id>")
    #     self.assertEqual(result.status_code, 200)
    #     self.assertIn('<h1>Photo Details</h1>', result.data)

if __name__ == "__main__":
    unittest.main()
