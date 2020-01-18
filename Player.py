class Player:

    def __init__(self, typ):
        self.typ = typ

    def to_string(self):
        return self.typ

    def to_int(self):
        if self.typ is "X":
            return 1
        else:
            return 2