# todo_service.py

import unittest
from unittest.mock import patch, MagicMock

from src.services import TodoService


class TestTodoService(unittest.TestCase):
    @patch('src.repository.TodoRepository')
    def test_save_todos_as_csv(self, mock_repo):
        mock_repo.find_all.return_value = [MagicMock()]
        service = TodoService(mock_repo)
        with patch('builtins.open', unittest.mock.mock_open()) as mocked_file:
            service.save_todos_as_csv()
            mocked_file.assert_called_once()
            # Agrega más aserciones para verificar la escritura correcta en el archivo


if __name__ == '__main__':
    unittest.main()
