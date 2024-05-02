#!/usr/bin/python3
"""
0-main
"""


def canUnlockAll(boxes):
    """
    Initialize a set to keep track of boxes we can unlock
    """
    unlocked_boxes = {0}
    """
    Iterate through the boxes
    """
    for box_num in range(len(boxes)):
        """
        if we can unlock the current box
        """
        if box_num in unlocked_boxes:
            """
            Add all keys in the current box to the set of unlocked boxes
            """
            unlocked_boxes.update(boxes[box_num])
    """
    Check if all boxes can be unlocked
    """
    return len(unlocked_boxes) == len(boxes)
