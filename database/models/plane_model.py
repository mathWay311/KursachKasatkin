class PlaneModel():
    def __init__(self, line):
        self.id = int(line[0])
        self.brand = line[1]
        self.model = line[2]
        self.board_number = line[3]
        self.isOccupied = bool(int(line[4]))
        self.isRepaired = bool(int(line[5]))
        self.malfunction = line[6]
        self.imgPath = line[7]
    def print_status(self):
        text = ""
        if self.isOccupied and self.isRepaired:
            text+= "Статус: Ремонтируется\n"
        elif self.isOccupied:
            text += "Статус: В полёте\n"
        else:
            text+= "Статус: Простаивает\n"

        if self.isRepaired:
            text += "Неисправен"
        else:
            text += "Исправен"

        return text