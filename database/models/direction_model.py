class DirectionModel():
    def __init__(self, line):
        self.id = int(line[0])
        self.from_ = line[1]
        self.to_ = line[2]