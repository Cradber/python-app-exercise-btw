# test_todo_repository.py

import unittest
from unittest.mock import MagicMock

from src.models.todo import Todo
from src.repository import TodoRepository


class TestTodoRepository(unittest.TestCase):
    def setUp(self):
        api_client = MagicMock()
        api_client.fetch_todos.return_value = [
            {'id': 1, 'userId': 1, 'title': 'Test Todo', 'completed': False}
        ]
        self.repo = TodoRepository(api_client)

    def test_find_all(self):
        todos = self.repo.find_all()
        self.assertEqual(len(todos), 1)
        self.assertIsInstance(todos[0], Todo)


if __name__ == '__main__':
    unittest.main()
