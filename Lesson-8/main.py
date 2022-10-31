#!/usr/bin/env python

class Friends:
    def __init__(self):
        self.people = []

    def add_friend(self, person):
        self.people.append(person)

    def __add__(self, other):
        self.add_friend(other)

        return self

    def __str__(self):
        s = "Group:"
        for person in self.people:
            s += "\n - " + str(person)
        return s

class Person:
    def __init__(self, one, two):
        self.name = one
        self.age = two
        self.fav_number = 32

    def __str__(self):
        return f"Person({self.name},{self.age})"

    def __add__(self, other):
        friends = Friends()
        friends.add_friend(self)
        friends.add_friend(other)
        return friends


    def bark(self):
        print(f"[{self.name}]: Woof!")

# create some people
mazunki = Person("Mazunki", 25)
harald = Person("Harald", 99)
anna = Person("Anna", 23)
rachel = Person("Rachel", 27)

friends = mazunki + anna
print(friends)

bigger_group = friends + rachel
print(bigger_group)


