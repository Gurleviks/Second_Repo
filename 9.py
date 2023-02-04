def greets(name="John", surname="Doe", family_list=[]):
    print(f"Hello {name} {surname}!")
    for member in family_list:
        print(f"Hello {member[0]} {member[1]}!")

greets()

family = [("Tristram", "Mcbride"), ("Baldwin", "Preston"), ("Wally", "Collins")]
greets(family_list=family)
