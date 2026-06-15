name = input("enter your name :")

match name:
    case "harry" | "Rom":
        print("Gryffindor")


    #case "harry":
        #print("Gryffindor")

    #case "Rom":
        #print("Gryffindor")

    case "Draco":
        print("slytherin")

    case _:
        print("Who?")       
            