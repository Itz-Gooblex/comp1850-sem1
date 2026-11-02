# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, fname:str=None, birthday:date=None):
        """
        Constructor passes inputted fullname and birthday
        """
        if type(fname) != str:
            raise TypeError("Name entered is not a valid name")

        if fname.isdigit():
            raise TypeError("Name entered is not a valid name")

        if not fname:
            raise ValueError("Name entered is nothing")

        self.name = fname

        if type(birthday) != date:
            raise TypeError("Date entered is not a date object")
            
        self.birth = birthday

    # Implement methods initials() and is_birthday() here
    def initials(self):
        """
        Take first letter of each word captialised
        """
        return "".join([word[0] for word in self.name.split(" ")]).upper()

    def is_birthday(self):
        """
        Return result of conditional statement, birthday == today
        """
        return self.birth.month == self.birth.today().month and self.birth.day == self.birth.today().day
    # (see README.md for further details)
