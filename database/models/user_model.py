class UserModel():
    def __init__(self, line):
        self.id = int(line[0])
        self.login = line[1]
        self.password = line[2]
        self.role = line[3]
        self.full_name = line[4]
        self.info = line[5]
        self.crewID = int(line[6])
