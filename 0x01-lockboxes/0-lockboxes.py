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
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for n in range(len(boxes)):
            boxes_checked = k in boxes[n] and k != n
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
