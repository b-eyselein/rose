from base.robot import Robot


def run_robot(robot: Robot, width: int, height: int) -> None:
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
