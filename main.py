#!/usr/bin/env python3

import argparse
import json
from typing import List

from adapter import adapt_run
from base.field import Field, Colors
from base.result import RoseResult, RobotResult
from base.robot import Robot
from base.testdata import TestData, load_test_data
from base.validation import validate
from sample import run_robot as sample_run
from solution import run_robot as user_run
from visualize import visualize


def run_robots(cur_test_data: TestData) -> RoseResult:
    field_options = cur_test_data.field_opts

    sample_field = Field(field_options.x, field_options.y)
    sample_robot = Robot('sample_robot', sample_field, cur_test_data.start, Colors.RED)
    adapt_run(sample_robot, cur_test_data.run_options, sample_run)

    # Inst. fields for both robots
    user_field = Field(field_options.x, field_options.y)
    user_robot = Robot('user_robot', user_field, cur_test_data.start, Colors.BLUE)
    adapt_run(user_robot, cur_test_data.run_options, user_run)

    return RoseResult(result_id=cur_test_data.id, correct=validate(user_field, sample_field),
                      start=cur_test_data.start, field_size=field_options,
                      sample_result=RobotResult(sample_robot.name, sample_robot.actions),
                      user_result=RobotResult(user_robot.name, user_robot.actions))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TODO!")
    parser.add_argument('--visualize', dest='visualize', default=False, action='store_true')
    args = parser.parse_args()

    with open('testdata.json', 'r') as file, open('result.json', 'w') as actions_file:

        test_data_list: List[TestData] = load_test_data(json.loads(file.read()))

        results: List[RoseResult] = []

        for test_data in test_data_list:
            results.append(run_robots(test_data))

        actions_file.write(json.dumps(list(map(lambda x: x.to_json(), results))))

        if args.visualize:
            visualize(results)
