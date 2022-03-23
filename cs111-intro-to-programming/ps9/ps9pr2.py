#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A class to represent calendar dates   
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    def tomorrow(self):
        '''returns the date after self'''
        
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.day += 1
        
        if self.is_leap_year() == True:
            days_in_month[2] == 29
        
        if self.day > days_in_month[self.month]:
            if self.month == 12:
                self.day = 1
                self.month = 1
                self.year += 1
            else:
                self.month += 1

    def add_n_days(self, n):
        '''prints the number of dates given by n followng and including self'''
        
        print(self)
        while n > 0:
            self.tomorrow()
            print(self)
            n -= 1

    def __eq__(self, other):
        '''returns true if both self and other are the same date'''
        
        if self.day == other.day:
            if self.month == other.month:
                if self.year == other.year:
                    return True
        return False

    def is_before(self,other):
        '''returns false if self is after or equal to other
        and true if self is before other''' 
        if self.__eq__(other):
            return False
        
        elif self.year < other.year:
            return True
        
        elif self.year == other.year:
            if self.month < other.month:
                    return True
                
            elif self.month == other.month:
                if self.day < other.day:
                    return True
          
        else:
            return False

        
    def is_after(self, other):
        '''returns false if self is before or equal to other
        and tru if self is after other'''
        
        if self.__eq__(other):
            return False
        elif self.is_before(other):
            return False
        return True

    def diff(self, other):
        '''returns number of days between two dates: self and other'''
        
        day_1 = self.copy()
        day_2 = other.copy()
        diff = 0
        
        if self.is_after(other):
            while day_1 != day_2:
                day_1.tomorrow()
                diff += -1
    
        else:
            while day_1 != day_2:
                day_2.tomorrow()
                diff += 1

        return diff

    def day_of_week(self):
        """Returns the day of the week of Date"""

        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                     'Friday', 'Saturday', 'Sunday']
        sunday = Date(4, 9, 2016)
        days_btw = self.diff(sunday)
        day_of_week = 0

        if days_btw < 0:
            days_btw*-1

        if days_btw > 0:
            while days_btw != 0:
                days_btw -= 1
                if day_of_week == 6:
                    day_of_week = 0
                else:
                    day_of_week += 1

        return day_of_week_names[day_of_week]
        


