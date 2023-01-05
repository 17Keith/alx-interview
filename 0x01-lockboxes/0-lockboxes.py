#!/usr/bin/python3

"""A number of locked boxes in front of you.\
     Each box is numbered sequentially from 0 to n - \
        and each box may contain keys to the other boxes."""


def canUnlockAll(boxes):
    """A method to determine if all the boxes can be opened"""
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
