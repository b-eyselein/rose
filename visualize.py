import sys
from tkinter import Tk, Canvas, Label, Frame, Button, LEFT
from typing import List

from base.actions import Action, MarkAction, MoveAction
from base.field import Direction, Vector2D
from base.result import RoseResult


class CanvasField(Frame):
    def __init__(self, **kw):
        super().__init__(**kw)


class RobotCanvas(Canvas):
    def __init__(self, field_size: Vector2D, column: int, cell_size: int, initial_pos: Vector2D, **kw):
        super().__init__(width=field_size.x * cell_size, height=field_size.y * cell_size, **kw)

        self.field_size: Vector2D = field_size

        self.width_in_pix = field_size.x * cell_size
        self.height_in_pix = field_size.y * cell_size

        self.grid(row=1, column=column, padx=(25, 25), pady=(25, 25))
        self.create_rectangle(0, 0, self.width_in_pix, self.height_in_pix, fill='#ffffff')

        self.cell_size: int = cell_size

        self.robot_position: Vector2D = initial_pos

        # Vertical lines
        for x in range(cell_size, self.width_in_pix, cell_size):
            self.create_line(x, 0, x, self.height_in_pix, fill='#000000')

        # Horizontal lines
        for y in range(cell_size, self.height_in_pix, cell_size):
            self.create_line(0, y, self.width_in_pix, y, fill='#000000')

        robot_coords: (int, int) = self.position_to_top_left_coordinates(self.robot_position)

        self.robot = self.create_oval(robot_coords[0] + 5, robot_coords[1] + 5,
                                      robot_coords[0] + cell_size - 5, robot_coords[1] + cell_size - 5, fill='#0000ff')

    def position_to_top_left_coordinates(self, position: Vector2D) -> (int, int):
        return position.x * self.cell_size, (self.field_size.y - position.y - 1) * self.cell_size

    def execute_action(self, action: Action):
        if isinstance(action, MoveAction):
            self.move_robot(action.direction)
        elif isinstance(action, MarkAction):
            self.mark_field(action)
        else:
            print(type(action))

    def move_robot(self, direction: Direction) -> None:
        move_x: int = direction.movement_x()
        move_y: int = direction.movement_y()

        self.robot_position: Vector2D = Vector2D(self.robot_position.x + move_x, self.robot_position.y + move_y)
        self.move(self.robot, move_x * self.cell_size, -move_y * self.cell_size)

    def mark_field(self, action: MarkAction) -> None:
        self.create_rectangle(self.robot_position.x * self.cell_size,
                              (self.field_size.y - self.robot_position.y - 1) * self.cell_size,
                              (self.robot_position.x + 1) * self.cell_size,
                              (self.field_size.y - self.robot_position.y) * self.cell_size,
                              fill=action.color.value)


class ControlFrame(Frame):
    def __init__(self, gui: 'VisualizeGUI', **kw):
        super().__init__(**kw)

        self.play_button: Button = Button(self, text='Play', fg='green', command=gui.play)
        self.play_button.pack(side=LEFT)

        self.pause_button: Button = Button(self, text='Pause', fg='red', command=gui.pause)
        self.pause_button.pack(side=LEFT)


class VisualizeGUI(Tk):
    def __init__(self, result: RoseResult):
        super().__init__()
        self.result: RoseResult = result

        self.geometry('1600x900')
        self.update()
        self.is_playing: bool = False

        self.current_step: int = 0

        min_outer = min((self.winfo_width() - 100) // 2, self.winfo_height() - 100)

        user_label = Label(self, text='Nutzerroboter')
        user_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        sample_label = Label(self, text='Musterroboter')
        sample_label.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))

        cell_size: int = min(min_outer // result.field_size.x, min_outer // result.field_size.y)

        self.user_canvas: RobotCanvas = RobotCanvas(result.field_size, 0, cell_size, result.start)
        self.sample_canvas: RobotCanvas = RobotCanvas(result.field_size, 1, cell_size, result.start)

        self.control_frame: ControlFrame = ControlFrame(gui=self)
        self.control_frame.grid(row=3, columnspan=2)

        self.update()

    def step_on(self) -> None:
        if self.current_step < len(self.result.user_result.actions):
            user_action: Action = self.result.user_result.actions[self.current_step]
            self.user_canvas.execute_action(user_action)

        if self.current_step < len(self.result.sample_result.actions):
            sample_action: Action = self.result.sample_result.actions[self.current_step]
            self.sample_canvas.execute_action(sample_action)

        if self.current_step >= len(self.result.user_result.actions) and self.current_step >= len(
                self.result.sample_result.actions):
            # Last action in bots results reached, stop
            self.is_playing = False

        self.current_step += 1

        if self.is_playing:
            self.after(300, self.step_on)

    def pause(self) -> None:
        print('Pausing', file=sys.stderr)
        self.is_playing = False

    def play(self) -> None:
        if self.is_playing:
            print('Already playing!', file=sys.stderr)
        else:
            self.is_playing = True
            self.step_on()


def visualize(results: List[RoseResult]) -> None:
    if len(results) == 0:
        return

    result: RoseResult = results[0]

    root = VisualizeGUI(result)
    root.mainloop()
