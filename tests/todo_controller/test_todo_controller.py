import unittest
from unittest.mock import patch
from src.controllers import TodoController


class TestTodoController(unittest.TestCase):
    @patch('src.api.TodoAPIClient.fetch_todos')
    def test_save_todos_as_csv(self, mock_fetch_todos):
        # Configura el mock para devolver datos de prueba
        mock_fetch_todos.return_value = [
            {'id': 1, 'userId': 1, 'title': 'Test Todo', 'completed': False}
        ]

        # Ahora al inicializar TodoController, fetch_todos está mockeado
        controller = TodoController("https://fake_api")
        # Supongamos que save_todos_as_csv no devuelve nada y solo queremos asegurar que no hay errores
        controller.save_todos_as_csv()

        # Verifica que el mock fue llamado, lo que implica que la lógica del controlador se ejecutó como se esperaba
        mock_fetch_todos.assert_called()


if __name__ == '__main__':
    unittest.main()
