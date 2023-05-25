class CrewModel():
    def __init__(self, line):
        self.id = int(line[0])
        self.name = line[1]
        self.pilotstring = line[2]
        self.stuardstring = line[3]
        self.isOccupied = bool(int(line[4]))

    def print_status(self):
        text = ""
        if self.isOccupied:
            text+= "Статус: Занят\n"
        else:
            text+= "Статус: Свободен\n"

        return text