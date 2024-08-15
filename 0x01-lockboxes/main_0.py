#!/usr/bin/python3

can_unlock_all = __import__('0-lockboxes').can_unlock_all

boxes = [[1], [2], [3], [4], []]
print(can_unlock_all(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(can_unlock_all(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(can_unlock_all(boxes))
