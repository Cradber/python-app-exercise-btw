# tests/test_apiservice.py

import unittest
from datetime import datetime
from unittest.mock import patch
from src.services.ApiService import ApiService
import os


class TestApiService(unittest.TestCase):

    def setUp(self):
        """Setup before each test."""
        self.api_service = ApiService()
        self.test_todo = {"userId": 1, "id": 1, "title": "Test TODO", "completed": False}

    @patch('requests.get')
    def test_get_all_todos(self, mock_get):
        """Test to verify that all TODOs can be fetched correctly."""
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = [self.test_todo]

        todos = self.api_service.get_all_todos()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0], self.test_todo)

    @patch('requests.get')
    def test_get_all_todos_failed(self, mock_get):
        """Test error handling when the API returns an error."""
        mock_get.return_value.ok = False
        mock_get.return_value.raise_for_status.side_effect = Exception("API failure")

        with self.assertRaises(Exception) as context:
            self.api_service.get_all_todos()

        self.assertTrue('API failure' in str(context.exception))

    def test_save_todo_as_csv(self):
        """Test to verify that a TODO is correctly saved in a CSV file."""
        # Create a temporary directory for CSV files
        temp_storage_path = 'temp_storage'
        os.makedirs(temp_storage_path, exist_ok=True)

        # Directly generate the date prefix here
        date_prefix = datetime.now().strftime("%d_%m_%Y")

        self.api_service.save_todo_as_csv(self.test_todo, temp_storage_path)

        # Construct the expected file name using the date prefix generated above
        expected_filename = f"{date_prefix}_{self.test_todo['id']}.csv"
        expected_filepath = os.path.join(temp_storage_path, expected_filename)

        # Verify the file was created
        self.assertTrue(os.path.exists(expected_filepath))

        # Cleanup: remove the file and temporary directory after the test
        os.remove(expected_filepath)
        os.rmdir(temp_storage_path)


if __name__ == '__main__':
    unittest.main()
