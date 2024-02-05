'''
original code with errors:


class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

def produce_people():
    from data import ages, names, locations

    people_list = []

    for n, a, l in name, age, location:
        person_instance = Person(name=n, age=a, location=l)
        people_list.append(person_instance)

    return people_list


results = produce_people()

for result in results:
    print(result)
'''
class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

def produce_people():
    from data import age, name, location # check the correct names in data

    people_list = []

    for n, a, l in zip(name, age, location):    # we need to zip the date, to get a table, and not just renaming them
        person_instance = Person(name=n, age=a, location=l)
        people_list.append(person_instance)

    return people_list


results = produce_people()

for result in results:
    print(result)
    # you can print the content of the class-instance with instance.__dict__
    print(result.__dict__)