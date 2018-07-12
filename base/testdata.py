from typing import List, Any

from jsonschema import validate

from base.field import Vector2D

test_data_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "start": {
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"}
                },
                "required": ["x", "y"]
            },
            "field": {
                "type": "object",
                "properties": {
                    "width": {"type": "number"},
                    "height": {"type": "number"}
                },
                "required": ["width", "height"]
            },
            "run_options": {}
        },
        "required": ["id", "start", "field", "run_options"]
    }
}


class TestData:
    def __init__(self, id: int, start: Vector2D, field_opts: Vector2D, run_options: Any):
        self.id: int = id
        self.start: Vector2D = start
        self.field_opts: Vector2D = field_opts
        self.run_options = run_options


def load_test_data(json_test_data_list) -> List[TestData]:
    validate(json_test_data_list, test_data_schema)

    td: List[TestData] = []

    for json_test_data in json_test_data_list:
        start = Vector2D(json_test_data['start']['x'], json_test_data['start']['y'])
        field_opts = Vector2D(json_test_data['field']['width'], json_test_data['field']['height'])

        td.append(TestData(json_test_data['id'], start, field_opts, run_options=json_test_data['run_options']))

    return td
