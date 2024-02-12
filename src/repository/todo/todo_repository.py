from src.api import TodoAPIClient
from src.models import Todo


class TodoRepository:
    def __init__(self, api_client: TodoAPIClient):
        self.api_client = api_client
        self.todos = self.api_client.fetch_todos()

    def find_all(self) -> [Todo]:
        return list(map(self._map_to_domain_entity, self.todos))
        # return [self._map_to_domain_entity(todo) for todo in todos_data]

    def _map_to_domain_entity(self, todo_data) -> Todo:
        return Todo(id=todo_data['id'], user_id=todo_data['userId'], title=todo_data['title'], completed=todo_data['completed'])
