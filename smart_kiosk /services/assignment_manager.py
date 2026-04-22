class AssignmentManager:
    def __init__(self) -> None:
        pass

    def all(self) -> list[dict]:
        return list(self.assignments)
        

    def add(self, title: str, description: str,
            points: int, assignment_type: str):
        pass

    def delete(self, assignment_id: str):
        pass