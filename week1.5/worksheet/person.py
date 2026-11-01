# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, fname:str, dob:date):
        if type(fname) != str:
            raise TypeError("Name entered is not a valid name")

        if  fname.isdigit():
            raise TypeError("Name entered is not a valid name")

        self.name = fname

        if type(dob) != date:
            raise TypeError("Date entered is not a date object")
            
        self.DOB = dob

    # Implement methods initials() and is_birthday() here
    def initials(self):
        return "".join([word[0] for word in self.name.split(" ")])

    def is_birthday(self):
        return self.DOB == self.DOB.today()
    # (see README.md for further details)

test = Person("Johnny English", date(2007, 10, 12))
print(test.initials())
print(test.is_birthday())
