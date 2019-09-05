from base.robot import Robot


def run_sample_robot(robot: Robot, height: int, width: int):
    for h in range(height - 1):
        robot.mark()
        robot.go_up()

    for w in range(width - 1):
        robot.mark()
        robot.go_right()

    for h in range(height - 1):
        robot.mark()
        robot.go_down()

    for w in range(width - 1):
        robot.mark()
        robot.go_left()
