import unittest
from server import app


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
