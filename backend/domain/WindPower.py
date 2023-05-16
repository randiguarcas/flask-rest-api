import re

class WindPower:
    def __init__(self, name, value):
        match = re.search(r'\((.*?)%\)', name)
        self.name = name
        self.value = value

        if match:
            self.percentage = float(match.group(1))
