#!/usr/bin/python3
"""
Script that checks if boxes can be opened
"""


def canUnlockAll(boxes):
    """
    The function `canUnlockAll` checks if all the boxes in a given list can
    be unlocked by using the keys inside the boxes.
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
