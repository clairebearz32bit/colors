import sys

from color import Color
#
#
# class Color:
#     COLORS = {
#         "BLACK": 0,
#         "RED":1,
#         "GREEN":2,
#         "YELLOW":3,
#         "BLUE":4
#     }
#
#     MODES = {
#         "FOREGROUND": 3
#     }
#
#     def __init__(self):
#         # "\u001b[31mRed Text\u001b[0m"
#         self.BASIC = "\u001b[{:1d}{1d}m{text}"
#         self.ESCAPE = self.BASIC + "0m"
#         # self.color
#         pass
#
#     def color(self, string, mode, color):
#         colored_string = "\u001b[{}{}m{}\u001b[0m".format(self.MODES[mode], self.COLORS[color], string)
#         return colored_string


if __name__ == '__main__':
    c = Color()
    mode = "FOREGROUND"
    color = "MAGENTA"
    string1 = "Test"
    print(c.color(string1, mode=mode,color=color))
