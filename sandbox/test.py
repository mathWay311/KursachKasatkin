def alter_record(id, column_id, text):
    lines = ["1;Boeing;737MAX8;RA-12345;0;0;PIZDA;b738ra12345.jpg;", "2;Boeing;737MAX8;RA-12345;0;0;PIZDA;b738ra12345.jpg;"]
    for line in lines:
        line = line.strip()
        args = line.split(";")
        if args[0] == id:
            args[column_id] = text
        output = ""

        for arg in args:
            output += str(arg) + ";"


        print(output)

alter_record("1",2,"Airbus")