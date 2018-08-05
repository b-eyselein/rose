from typing import List

from base.actions import Action
from base.field import Vector2D


class RobotResult:
    def __init__(self, name: str, actions: List[Action]):
        self.name: str = name
        self.actions: List[Action] = actions

    def to_json(self):
        return {
            'name': self.name,
            'size': len(self.actions),
            'actions': list(map(str, self.actions))
        }


class RoseResult:
    def __init__(self, result_id: int, correct: bool, start: Vector2D, field_size: Vector2D, sample_result: RobotResult,
            user_result: RobotResult):
        self.id: int = result_id
        self.correct: bool = correct
        self.start: Vector2D = start
        self.field_size: Vector2D = field_size
        self.sample_result: RobotResult = sample_result
        self.user_result: RobotResult = user_result

    def to_json(self):
        return {
            'id': self.id,
            'correct': self.correct,
            'start': self.start.to_json(),
            'fieldSize': self.field_size.to_json(),
            'sampleResult': self.sample_result.to_json(),
            'userResult': self.user_result.to_json()
        }
