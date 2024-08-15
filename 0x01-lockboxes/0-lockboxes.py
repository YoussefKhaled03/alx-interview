#!/usr/bin/python3
'''LockBoxes Challenge'''


def can_unlock_all(boxes):
    """
    Checks if all the boxes in the given list can be unlocked.
    Args:
        boxes (list): A list of lists representing the lockboxes and their corresponding keys.
    Returns:
        bool: True if all the boxes can be unlocked, False otherwise.
    """
    opened_boxes = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                stack.append(key)

    return len(opened_boxes) == len(boxes)
