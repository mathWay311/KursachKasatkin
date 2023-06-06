class Model:
    def __init__(self, line : list):
        pass

class FlightModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.planeID = int(line[1])
        self.date_start = line[2]
        self.date_end = line[3]
        self.directionID = int(line[4])
        self.crewID = int(line[5])
        self.isStarted = bool(int(line[6]))
        #
        self.crewName = ""
        self.planeName = ""
        self.dirName = ""

    def print(self):
        return self.dirName + " выполняющийся на самолёте " + self.planeName + " экипажем " + self.crewName


class PlaneModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.brand = line[1]
        self.model = line[2]
        self.board_number = line[3]
        self.isFlying = bool(int(line[4]))
        self.isRepaired = bool(int(line[5]))
        self.malfunction = line[6]
        self.imgPath = line[7]
        self.isBinded = bool(int(line[8]))

    def print_status(self):
        text = ""
        if not self.isBinded and not self.isFlying and not self.isRepaired:
            text = "Статус: Не назначен на рейс\nИсправен"
        elif self.isBinded and not self.isFlying and not self.isRepaired:
            text = "Статус: Назначен на рейс\nИсправен"
        elif self.isBinded and self.isFlying and not self.isRepaired:
            text = "Статус: В полёте\nИсправен"
        elif not self.isBinded and not self.isFlying and self.isRepaired:
            text = "Статус: На ремонте\nНеисправен"
        elif self.isRepaired and self.isBinded and self.isFlying:
            text = "Статус: В полёте, но назначен на ремонт\nНеисправен"
        elif self.isBinded and self.isRepaired and not self.isFlying:
            text = "Статус: Назначен на рейс, но ремонтируется\nНеисправен"
        else:
            text = "Статус: Ошибочный. Свяжитесь с администратором\n"


        return text

class UserModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.login = line[1]
        self.password = line[2]
        self.role = line[3]
        self.full_name = line[4]
        self.info = line[5]
        self.crewID = int(line[6])

class DirectionModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.from_ = line[1]
        self.to_ = line[2]

class CrewmemberModel(Model):
    def __init__(self, line):
        super().__init__(line)
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
        self.isBindedToCrew = bool(int(line[10]))
        self.isInFlight = bool(int(line[11]))

    def print_status(self):
        text = "Статус: "
        if self.isInFlight:
            text += "Сейчас в полёте. "
        if self.isOccupied:
            text += "Принадлежит экипажу, назначенному на рейс. "
        if self.isBindedToCrew:
            text += "Назначен на экипаж. "
        if self.isRetired:
            text += "В отпуске. "
        if not self.isRetired and not self.isOccupied and not self.isBindedToCrew and not self.isInFlight:
            text += "Не назначен в экипаж"

        return text

class CrewModel(Model):

    def __init__(self, line):
        super().__init__(line)
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