def insert_degree_program(db,degreeName):
    if degreeName in db: 
        print(f"{degreeName} is already in the database")
    else: 
        db[degreeName]= {}


def insert_course(db,degreeName,course):

    name, credit = course
    if name in db[degreeName]: #course is a tuple, so name can be used directly
    # cannot access tuple by course[name] because it is not a dictionary 
        print(f"{name} is already in the database")
    else:
        db[degreeName][name]= credit #get in the degreename dict's key, then get into the name key = key of courses 
        


def print_degree_program(db,degreeName):
    print(f"{degreeName} ({len(db[degreeName])} courses)")
    totalcredits = 0
    for name,credit in (db[degreeName].items()):
        print(f"   {name}, {credit} credits")
        totalcredits += credit
    print(f"   Total credits: {totalcredits}")

def main():
    db = {} 
    insert_degree_program(db, "ITBBA") 
    insert_degree_program(db, "EXPER")

    insert_course(db, "ITBBA", ("Python Programming", 5)) 
    insert_course(db, "ITBBA", ("Time Management", 3)) 
    insert_course(db, "EXPER", ("Creative Hospitality and Tourism", 5)) 
    insert_course(db, "EXPER", ("Managing Dynamic Restaurant Business", 10)) 
    
    print_degree_program(db, "ITBBA") 
    print_degree_program(db, "EXPER")

    remove_course(db, "ITBBA", "Python Programming")
    print_degree_program(db, "ITBBA")     
    print()       #Testing error handling     
    insert_degree_program(db, "ITBBA")     
    insert_course(db, "ITBBA", ("Time Management", 3))
    print_degree_program(db, "LOBBY")
    remove_course(db, "COMPU", "Surfing")
    remove_course(db, "ITBBA", "Surfing")  

main()
                          