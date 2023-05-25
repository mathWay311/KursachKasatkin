class FlightModel():
    def __init__(self, line):
        self.id = int(line[0])
        self.planeID= int(line[1])
        self.date_start = line[2]
        self.date_end = line[3]
        self.directionID = int(line[4])
        self.crewID = int(line[5])
        #
        self.crewName = ""
        self.planeName = ""
        self.dirName = ""
    def print(self):
        return self.dirName + " выполняющийся на самолёте " + self.planeName + " экипажем " + self.crewName