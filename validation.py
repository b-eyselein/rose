from field import Field, Cell


def __compare_cells__(user_cell: Cell, sample_cell: Cell, mind_colors: bool) -> bool:
    if mind_colors:
        return user_cell.color == sample_cell.color
    else:
        return user_cell.is_marked() == sample_cell.is_marked()


def __fields_equal__(user_field: Field, sample_field: Field, mind_colors: bool = False) -> bool:
    if user_field.height != sample_field.height or user_field.width != sample_field.width:
        return False

    for row_index in range(user_field.height):
        for cell_index in range(user_field.width):
            user_cell = user_field.get(row_index, cell_index)
            sample_cell = sample_field.get(row_index, cell_index)
            if not __compare_cells__(user_cell, sample_cell, mind_colors):
                return False
    return True


def validate(user_field: Field, sample_field: Field, mind_colors: bool) -> bool:
    return __fields_equal__(user_field, sample_field, mind_colors)
