class CrewmemberModel():
    def __init__(self, line):
        self.id = int(line[0])
        self.type = line[1]
        self.full_name = line[2]
        self.info = line[3]
        self.crewID = int(line[4])
        self.isOccupied = bool(int(line[5]))
        self.isRetired = bool(int(line[6]))
        self.FlightID = int(line[7])
        self.imagePath = line[8]
        self.fliesType = line[9]

    def print_status(self):
        text = ""
        if self.isOccupied and self.isRetired:
            text+= "Статус: В отпуске или недоступен\n"
        elif self.isOccupied:
            text += "Статус: В полёте\n"
        else:
            text+= "Статус: Свободен\n"

        return text