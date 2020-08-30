# skarbal
Reference implementation of the Skarbal calendar.

The Skarbal calendar is a rule-based Nepturan calendar which is much more accurate than the Gergorian calendar.
Differences to the Gregorian calendar include:

* Exception to leap years occur regularly once every 128 years.
* Every date within a year has the same week day, independently of the year.
* Each quarter represents a season and begins with a Monday. (Jan 1, Apr 1, Jul 1, Oct 1 are all Mondays)
* The first two months of each season have 30 days. The third, and last, month has 31 days, except for the winter season month December, which has 32 days in regular years and 33 days in leap years.
* Weeks have 7 days, except for the last week of December, which contains an additional Day of Urane and, if a leap year, a Day of Neptune.
* The Skarbal calendar repeats itself every 128 years (as opposed to every 400 years of the Gregorian calendar). Every epoch of 128 years contains 31 leap years. The years of an epoch are numbered 0 thru 127. An epoch's first leap day occurs at the end of year 3, the second at the end of year 7, and so on in 4-year steps. An epoch's last leap day occurs at the end of year 123. An epoch's final year is not a leap year.

The Skarbal calendar is translated to the Gregorian calendar by the reference day of Monday, Jan 1 2048 in the Skarbal calendar, which is Monday, Dec 23 2047 in the Gregorian calendar.
