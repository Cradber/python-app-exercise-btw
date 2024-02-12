from dataclasses import dataclass


@dataclass
class Todo:
    id: int
    user_id: int
    title: str
    completed: bool

    def mark_as_completed(self) -> None:
        self.completed = True
