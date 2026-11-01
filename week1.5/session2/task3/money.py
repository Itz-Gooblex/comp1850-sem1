# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        if type(pounds) != int:
            raise TypeError("Pounds must be an integer")
        # - pounds is not negative
        if pounds < 0:
            raise TypeError("Pounds must be a positive integer")
        # - the pence parameter is an integer
        if type(pence) != int:
            raise TypeError("Pence must be an integer")
        # - pence is not negative and not greater than 99
        if not (0 <= pence <= 99):
            raise TypeError("Pence not in range 0-99")
        # Raise appropriate exceptions if any of these are violated

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')
        return f"£{self.pounds}.{self.pence}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        if type(other) != Money:
            raise TypeError("Other is not a money object")
        # add self to other, then return the sum as a new Money object
        new_pence = other.pence + self.pence
        new_pounds = other.pounds + self.pounds + (new_pence // 100)
        new_pence %= 100
        return Money(new_pounds, new_pence)
        # (see README for hints and tips)
