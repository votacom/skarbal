# "the epoch" is Monday, Dec 23, 2047 (Gregorian) == Monday, Jan 1, 2048 (Skarbal)
# leap years are every 4 years except every 128 years. At the end of year 3, there is a leap day. Year 4 starts a regular year. Year 0 has no leap day, because 0 is divisible by 128.
# a 128-year epoch starts with Jan 1 of the year that is divisible by 128 (e.g. Jan 1 1920) and ends with Dec 32 (e.g. 2047).

import datetime
import math

# returns the diff number of days to the Epoch. The input is interpreted as Gregorian. Its type is datetime.date.
def diff_greg(date):
    delta = date - datetime.date(2047, 12, 23)
    return delta.days

class Skarbaldate:
    def __init__(self, year=2048, month=1, day=1): #default is epoch
        self.year=year
        self.month=month
        self.day=day
    def fromgregorian(gregdate): #from gregorian date
        skar = Skarbaldate()
        skar.add(diff_greg(gregdate))
        return skar
    def update(self, gregdate):
        self.year=2048
        self.month=1
        self.day=1
        self.add(diff_greg(gregdate))

    def __repr__(self):
        return 'Skarbaldate({},{},{})'.format(self.year, self.month, self.day)

    def __str__(self):
        return '{}, {}-{:02d}-{:02d}'.format(self.strdow(), self.year, self.month, self.day)

    def diff(self): #returns the number of days since the Epoch.
        leap_days = math.floor( (self.year - 2048) / 4 ) - math.floor( (self.year - 2048) / 128 ) #number of (full) leap days since the epoch
        num_days_until_jan1 = (self.year - 2048) * 365 + leap_days # number of days since the epoch until Jan 1 self.year.
        return num_days_until_jan1 + self.dayofyear() - 1

    def dayofyear(self): #returns the day of the year. 1 is Jan 1st.
        daysinfullmonths = (self.month-1) * 30 + math.floor( (self.month-1) / 3 )
        return daysinfullmonths + self.day

    def togregorian(self):
        greg = datetime.date(2047, 12, 23)
        greg += datetime.timedelta(days=self.diff())
        return greg
    
    def add(self, numdays): # adds the given number of days to this date.
        if( numdays == 0 ):
            return
        targetdiff = self.diff() + numdays
        if( numdays < 0 ):
            self.year -= 128
        else:
            #numdays>0.
            if( numdays >= 366 ):
                #advance a full year:
                self.year += 1
                # this day may not exist in the next year iff it's Dec 33.
                if( self.month == 12 and self.day == 33 ):
                    self.day = 32
            else:
                #advance day by day.
                self.advance()
        missingdiff = targetdiff - self.diff()
        self.add(missingdiff)
    def isleapyear(self):
        return self.year % 4 == 0 and self.year % 128 > 0
    def advance(self): # advance this date by 1 day.
        self.day += 1
        day_ok = self.day <= 30 or \
                 self.day == 31 and self.month in [3,6,9,12] or \
                 self.day == 32 and self.month == 12 or \
                 self.day == 33 and self.month == 12 and self.isleapyear()
        if( not day_ok ):
            self.day = 1
            self.month += 1
        month_ok = self.month <= 12
        if( not month_ok ):
            self.month = 1
            self.year += 1

    def dayofweek(self): #returns 1 (Monday) thru 9 (Day of Neptune)
        if( self.day == 32 ):
            return 8 # day of Urane
        if( self.day == 33 ):
            return 9 # day of Neptune / leap day
        return (self.dayofyear()-1) % 7 + 1

    def strdow(self): #returns day of week as English string
        dow = self.dayofweek()
        if( dow == 1 ):
            return 'Monday'
        if( dow == 2 ):
            return 'Tuesday'
        if( dow == 3 ):
            return 'Wednesday'
        if( dow == 4 ):
            return 'Thursday'
        if( dow == 5 ):
            return 'Friday'
        if( dow == 6 ):
            return 'Saturday'
        if( dow == 7 ):
            return 'Sunday'
        if( dow == 8 ):
            return 'Day of Urane'
        if( dow == 9 ):
            return 'Day of Neptune'

def main():
    greg = datetime.date.today()
    skar = Skarbaldate.fromgregorian(greg)

    while(True):
        print('Gregorian: {}'.format(greg.strftime('%a %x')))
        print('Skarbal: {}'.format(skar))
        command = input('>> ').strip()
        try:
            if( command == 'help' ):
                print('Accepted commands are:')
                print('a - advance date by 1 day')
                print('t - set to today')
                print('g YYYY-MM-DD - set date to given Gregorian date')
                print('s YYYY-MM-DD - set date to given Skarbal date')
            elif command == 'a':
                skar.advance()
                greg = skar.togregorian()
            elif command == 't':
                greg = datetime.date.today()
                skar = Skarbaldate.fromgregorian(greg)
            elif command.startswith('g '):
                greg = datetime.date.fromisoformat(command.split()[1])
                skar.update(greg)
            elif command.startswith('s '):
                date = command.split()[1]
                ymd = list(map(int, date.split('-')))
                skar = Skarbaldate(ymd[0], ymd[1], ymd[2])
                greg = skar.togregorian()
            else:
                print("Could not interpret command. Type `help` to see available commands.")
        except ValueError:
            print("A parsing error occured. Type `help` to see available commands.")

if __name__ == '__main__':
    main()

