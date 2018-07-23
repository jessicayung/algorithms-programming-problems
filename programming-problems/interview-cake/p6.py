def rectangular_intersection(rect1, rect2):
    """rect1 and rect2 are dictionaries."""

    # Initialise rectangle
    rect_intersection = {}

    # Put x coordinates into an array
    x_coordinates = [rect1['left_x'], rect1['left_x'] + rect1['width'], rect2['left_x'], rect2['left_x'] + rect2['width']]

    # Check two rectangles intersect in x
    if x_coordinates[1] < x_coordinates[2] and x_coordinates[3] < x_coordinates[1]:
        return False

    # Add rectangular intersection x values to rect_intersection dictionary
    x_coordinates = sorted(x_coordinates)
    rect_intersection['left_x'] = x_coordinates[1]
    rect_intersection['width'] = x_coordinates[2] - x_coordinates[1]

    # Put y coordinates into an array
    y_coordinates = [rect1['bottom_y'], rect1['bottom_y'] + rect1['height'], rect2['bottom_y'], rect2['bottom_y'] + rect2['height']]

    # Check two rectangles intersect in y
    if y_coordinates[1] < y_coordinates[2] and y_coordinates[3] < y_coordinates[0]:
        return False

    # Add rectangular intersection y values to rect_intersection dictionary
    y_coordinates = sorted(y_coordinates)
    rect_intersection['bottom_y'] = y_coordinates[1]
    rect_intersection['height'] = y_coordinates[2] - y_coordinates[1]

"""
Dumb way of doing it:

if rect1['left_x'] < rect2['left_x']:
    left_rect = rect1
    right_rect = rect2
elif rect1['left_x'] == rect2['left_x']:
    if rect1['width'] <= rect2['width']:
        left_rect = rect1
        right_rect = rect2
    else:
        left_rect = rect2
        right_rect = rect1
else:
    left_rect = rect2
    right_rect = rect1

# Find x intersection
if left_rect['left_x'] + left_rect['width'] < right_rect['left_x']:
    return False
"""