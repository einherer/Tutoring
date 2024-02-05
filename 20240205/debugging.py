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
    print(result.__dict__)