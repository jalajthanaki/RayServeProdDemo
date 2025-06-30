import unittest
from .key_manager import APIKeyManager

class TestAPIKeyManager(unittest.TestCase):
    def setUp(self):
        # Clean up all keys before each test
        for key in APIKeyManager.list_keys():
            APIKeyManager.delete_key(key)

    def test_create_key(self):
        key = APIKeyManager.create_key()
        self.assertIn(key, APIKeyManager.list_keys())

    def test_list_keys(self):
        key1 = APIKeyManager.create_key()
        key2 = APIKeyManager.create_key()
        keys = APIKeyManager.list_keys()
        self.assertIn(key1, keys)
        self.assertIn(key2, keys)

    def test_increment_usage(self):
        key = APIKeyManager.create_key()
        count1 = APIKeyManager.increment_usage(key)
        count2 = APIKeyManager.increment_usage(key)
        self.assertEqual(count1, 1)
        self.assertEqual(count2, 2)
        self.assertEqual(APIKeyManager.get_usage(key), 2)

if __name__ == "__main__":
    unittest.main()
