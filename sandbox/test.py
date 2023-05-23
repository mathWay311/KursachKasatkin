def query(self, query):
    args = query.split(" ")
    if len(args) == 4 and args[3] == "*":
        print("SELECT ALL FROM " + args[1])


query("", "FROM users SELECT *")
query("", "FROM users")