"""

General format:
\u001b[<style><color location>

"""

class Color:
    COLORS = {
        "BLACK": 0,
        "RED":1,
        "GREEN":2,
        "YELLOW":3,
        "BLUE":4,
        "MAGENTA": 5,
        "CYAN": 6,
        "WHITE": 7
    }

    MODES = {
        "FOREGROUND": 3,
        "BACKGROUND": 4,
        "BRIGHT": 9,
        "BRIGHT_BACKGROUND": 10
    }

    def __init__(self):
        # "\u001b[31mRed Text\u001b[0m"
        self.BASIC = "\u001b[{:1d}{1d}m{text}"
        self.ESCAPE = self.BASIC + "0m"
        # self.color
        pass

    def color(self, string, mode, color, **kwargs):
        STYLES = {
            "BOLD": 1

        }

        for i in kwargs:
        # "\u001b[31mRed Text\u001b[0m"
            pass

        colored_string = "\u001b[{}{}m{}\u001b[0m".format(self.MODES[mode], self.COLORS[color], string)
        return colored_string
