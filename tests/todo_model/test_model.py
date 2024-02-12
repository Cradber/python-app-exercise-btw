# test_todo.py

import unittest
from src.models.todo import Todo


class TestTodoModel(unittest.TestCase):
    def test_mark_as_completed(self):
        todo = Todo(id=1, user_id=1, title="Test Todo", completed=False)
        todo.mark_as_completed()
        self.assertTrue(todo.completed)


if __name__ == '__main__':
    unittest.main()
