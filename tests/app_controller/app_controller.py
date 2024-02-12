import unittest
from unittest.mock import patch
from src.controllers.app_controller import AppController


class TestAppController(unittest.TestCase):
    @patch('src.controllers.app_controller.TodoController')
    def test_save_todos_as_csv(self, mock_todo_controller):
        # Inicializa AppController, lo cual debería, a su vez, inicializar TodoController
        app_controller = AppController()

        # Llama al método que quieres probar
        app_controller.save_todos_as_csv()

        # Verifica que save_todos_as_csv en TodoController fue llamado una vez
        mock_todo_controller.return_value.save_todos_as_csv.assert_called_once()


if __name__ == '__main__':
    unittest.main()
