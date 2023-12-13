class Colors:
    gray = (32, 32, 32)
    magenta = (255, 0, 127)
    orange = (255, 128, 0)
    lila = (153, 153, 255)
    yellow = (255, 255, 0)
    light_green = (102, 255, 102)
    deep_green = (0, 153, 0)
    intense_red = (255, 0, 0)
    white = (255, 255, 255)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
        return [cls.gray, cls.magenta, cls.orange, cls.lila,
                cls.yellow, cls.light_green, cls.deep_green,
                cls.intense_red]
