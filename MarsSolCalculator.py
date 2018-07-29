#!/usr/bin/env python

"""MarsSolCalculator.py:
This code is meant to generate a Martian calendar when given landing date (sol 1). I am using it to write a sci-fi novel,
and I'm quite strict on accuracy, as I am a science student myself. With Google being around, no excuses for slacking!


It has a few functions:

- F1: Calculating a Martian calendar in Mars Years and sols, when given the Earth date of sol 1 (mission landing),
and the Earth date you want to calculate the output calendar for. This calendar includes seasons, and is adaptable to
being generated in the Northern & Southern hemisphere of Mars.

- F2: Calculating a Martian's age range in Earth years + days, when given a Martian Year of birth and the current date in
Earth Years (age range for the Martian school year, basically. Yeah, no escaping homework).

- F3: Converting input of Martian Years + Sols to Earth Years, and generating current season from that information too.


!!!!! CURRENT PROBLEMS:
- When I use F3 of the code and input a Mars Year + Sol, I get an Earth Year and date. But when I input this date into
F1 of the code, it generates a different Mars Year + Sol from the one inputted into F3. It is usually off by about 30 sols
when I have tried it. The seasons still accurately correspond to the given Mars Year + Sol date.
Theories:
- I made a mistake in the functions. I'm v tired.
- I should have been using sidereal days instead of solar days.
- Seasons and Years don't line up perfectly, but I don't see how that affects calendar dates.

!!!!! If anyone wants to add:
- A time difference clock for Earth to Mars time, and/or vice versa. Ideally using hours/min/sec for Earth,
and rotation degrees (out of 360degrees) as timekeeping on Mars.
- More accurate age converter

!!!!! Mathematical conversions are sourced in ### CONVERSION NUMBERS, subject to change with more accurate information.
Runs in python 3.6.
Not for professional purposes. Code author created this have accurate world building for a sci-fi novel. If anyone
likes to read sci-fi novels about the doom of a Mars colony and extreme human suffering hit me up!"""


__author__ = "Diane Magnin"
__version__ = "1.3"
__email__ = "dianemagnin@yahoo.com"
__twitter__ = "@DianeM97"


### CONVERSION DATA:
MarsYearInSols = 668.5921  #tropical year. Or 686.9725 Earth days, FYI.
SolInHours = 24.65979 #solar day. 1 Sol = 24 h, 39 min, 35.244 s. #Or 24h 37m 22.663s sidereal day, FYI.
# Data from: https://www.giss.nasa.gov/tools/mars24/help/notes.html
# EarthYearInDays = 365.25 self explanatory, takes Leap Years into account
# EarthDayInHours = 24 h. Solar day. Rounded up a tad.
# MARS SEASON LENGTHS:
#NHSpring_SHFall_length = 194 sols
#NHSummer_SHWinter_length = 178 sols
#NHFall_SHSpring_length = 142 sols
#NHWinter_SHSummer_length = 154 sols
# source: https://beamartian.jpl.nasa.gov/towhnall/question/14/does-mars-have-seasons-if-so-how-long-does-each-one-last



#=================================== ENTER INFO HERE

# When was SOL 1?
Sol_1_Earth_Year = 2067
Sol_1_Earth_Month = 6 # 1 being Jan, 2 being Feb etc...
Sol_1_Earth_Date = 10
# Seasonal information
Mars_Season_at_landing = 2 # Spring = 1, Summer = 2, Fall = 3, Winter = 4
Days_into_Mars_Season = 162
Hemisphere = "Northern" # "Northern" or "Southern", if on equator, choose "Northern"
# Above seasonal information is accurate for Sol 1 date 2067/06/10, according to
# http://www.planetary.org/explore/space-topics/mars/mars-calendar.html


# F1: What date do you want to generate a calendar for?
Date_to_calculate_AD = 2168
Date_to_calculate_Month = 3
Date_to_calculate_Day = 1


# F2: In which MARS YEAR was the colonist born?
MARS_BIRTH_YEAR = 44.6


# F3: Convert Mars Date to corresponding Earth Date
Date_to_calculate_MY = 53
Date_to_calculate_sol = 400

#======================================= END ENTER INFO






# -------------------- F1: Generate Earth Days to Mars Year Calendar

def leapYear(year):
    # detects Leap Year
    if year % 4 == 0:
        return True
    else:
        return False

def monthConversion(year, month):
    # converts input Month to number of days past since Jan 1st. So Feb 1st would be 31 days + 1 day.
    leap = leapYear(year)
    if leap:
        if month == 1:
            return(0)
        elif month == 2:
            return(31)
        elif month == 3:
            return(31+29)
        elif month == 4:
            return(31+29+31)
        elif month == 5:
            return(31+29+31+30)
        elif month == 6:
            return(31+29+31+30+31)
        elif month == 7:
            return(31+29+31+30+31+30)
        elif month == 8:
            return(31+29+31+30+31+30+31)
        elif month == 9:
            return(31+29+31+30+31+30+31+31)
        elif month == 10:
            return(31+29+31+30+31+30+31+31+30)
        elif month == 11:
            return(31+29+31+30+31+30+31+31+30+31)
        elif month == 12:
            return(31+29+31+30+31+30+31+31+30+31+30)
        else:
            return(0)
    else:
        if month == 1:
            return(0)
        elif month == 2:
            return(31)
        elif month == 3:
            return(31+28)
        elif month == 4:
            return(31+28+31)
        elif month == 5:
            return(31+28+31+30)
        elif month == 6:
            return(31+28+31+30+31)
        elif month == 7:
            return(31+28+31+30+31+30)
        elif month == 8:
            return(31+28+31+30+31+30+31)
        elif month == 9:
            return(31+28+31+30+31+30+31+31)
        elif month == 10:
            return(31+28+31+30+31+30+31+31+30)
        elif month == 11:
            return(31+28+31+30+31+30+31+31+30+31)
        elif month == 12:
            return(31+28+31+30+31+30+31+31+30+31+30)
        else:
            return(0)

#converting input/output month/day dates to number of days past Jan 1st
#
monthLanding = monthConversion(Sol_1_Earth_Year, Sol_1_Earth_Month)
Date_landing_in_days = monthLanding + Sol_1_Earth_Date
#
monthCalculating = monthConversion(Date_to_calculate_AD, Date_to_calculate_Month)
Date_to_calculate_in_days = monthCalculating + Date_to_calculate_Day
#
days_diff = Date_to_calculate_in_days - Date_landing_in_days

# generate calendar log: Earth date = X Mars Years + X Sols
Difference_in_years = Date_to_calculate_AD - Sol_1_Earth_Year
Difference_in_days = Difference_in_years*365.25 + days_diff
Difference_in_sols = Difference_in_days*24/SolInHours
Difference_in_MY = Difference_in_sols/MarsYearInSols
Date_year = int(Difference_in_MY)
Sols_date = (Difference_in_MY - Date_year) * MarsYearInSols

#Season calculator
#NHSpring_SHFall_length = 194, NHSummer_SHWinter_length = 178, NHFall_SHSpring_length = 142, NHWinter_SHSummer_length = 154

def SeasonCalculatorNh(landingseason, daysinto, sol_diff):
    #Calculate which season it will be in the future in the Northern Hemisphere, outputs a string
    Days_past = int((sol_diff+daysinto) % MarsYearInSols)
    print(Days_past)
    if landingseason == 1:
        if Days_past < 194:
            Days_gone = Days_past - 0
            return str("We are %d/194 sols into Spring!" % Days_gone)
        elif Days_past < 372:
            Days_gone = Days_past - 194
            return str("We are %d/178 sols into Summer!" % Days_gone)
        elif Days_past < 514:
            Days_gone = Days_past - 372
            return str("We are %d/142 sols into Fall!" % Days_gone)
        elif Days_past < 669:
            Days_gone = Days_past - 514
            return str("We are %d/154 sols into Winter!" % Days_gone)
    elif landingseason == 2:
        if Days_past < 178:
            Days_gone = Days_past - 0
            return str("We are %d/178 sols into Summer!" % Days_gone)
        elif Days_past < (178+142):
            Days_gone = Days_past - 178
            return str("We are %d/142 sols into Fall!" % Days_gone)
        elif Days_past < (178+142+154):
            Days_gone = Days_past - (178+142)
            return str("We are %d/154 sols into Winter!" % Days_gone)
        elif Days_past < 669:
            Days_gone = Days_past - (178+142+154)
            return str("We are %d/194 sols into Spring!" % Days_gone)
    elif landingseason == 3:
        if Days_past < 142:
            Days_gone = Days_past - 0
            return str("We are %d/142 sols into Fall!" % Days_gone)
        elif Days_past < (142+154):
            Days_gone = Days_past - 142
            return str("We are %d/154 sols into Winter!" % Days_gone)
        elif Days_past < (142+154+194):
            Days_gone = Days_past - (142+154)
            return str("We are %d/194 sols into Spring!" % Days_gone)
        elif Days_past < 669:
            Days_gone = Days_past - (142+154+194)
            return str("We are %d/178 sols into Summer!" % Days_gone)
    elif landingseason == 4:
        if Days_past < 154:
            Days_gone = Days_past - 0
            return str("We are %d/154 sols into Winter!" % Days_gone)
        elif Days_past < (154+194):
            Days_gone = Days_past - 154
            return str("We are %d/194 sols into Spring!" % Days_gone)
        elif Days_past < (154+194+178):
            Days_gone = Days_past - (152+194)
            return str("We are %d/178 sols into Summer!" % Days_gone)
        elif Days_past < 669:
            Days_gone = Days_past - (154+194+178)
            return str("We are %d/142 sols into Fall!" % Days_gone)

def SeasonCalculatorSh(landingseason, daysinto, sol_diff):
    # Calculate which season it will be in the future in the Southern Hemisphere, outputs a string
    Days_past = int(sol_diff % MarsYearInSols) + daysinto
    if landingseason == 3:
        if Days_past < 194:
            Days_gone = Days_past - 0
            return str("We are %d/194 sols into Autumn!" % Days_gone)
        elif Days_past < 372:
            Days_gone = Days_past - 194
            return str("We are %d/178 sols into Winter!" % Days_gone)
        elif Days_past < 514:
            Days_gone = Days_past - 372
            return str("We are %d/142 sols into Spring!" % Days_gone)
        elif Days_past < 669:
            Days_gone = Days_past - 514
            return str("We are %d/154 sols into Summer!" % Days_gone)
    elif landingseason == 4:
        if Days_past < 178:
            Days_gone = Days_past - 0
            return str("We are %d/178 sols into Winter!" % Days_gone)
        elif Days_past < (178+142):
            Days_gone = Days_past - 178
            return str("We are %d/142 sols into Spring!" % Days_gone)
        elif Days_past < (178+142+154):
            Days_gone = Days_past - (178+142)
            return str("We are %d/154 sols into Summer!" % Days_gone)
        elif Days_past < 669:
            Days_gone = Days_past - (178+142+154)
            return str("We are %d/194 sols into Fall!" % Days_gone)
    elif landingseason == 1:
        if Days_past < 142:
            Days_gone = Days_past - 0
            return str("We are %d/142 sols into Spring!" % Days_gone)
        elif Days_past < (142+154):
            Days_gone = Days_past - 142
            return str("We are %d/154 sols into Summer!" % Days_gone)
        elif Days_past < (142+154+194):
            Days_gone = Days_past - (142+154)
            return str("We are %d/194 sols into Fall!" % Days_gone)
        elif Days_past < 669:
            Days_gone = Days_past - (142+154+194)
            return str("We are %d/178 sols into Winter!" % Days_gone)
    elif landingseason == 2:
        if Days_past < 154:
            Days_gone = Days_past - 0
            return str("We are %d/154 sols into Summer!" % Days_gone)
        elif Days_past < (154+194):
            Days_gone = Days_past - 154
            return str("We are %d/194 sols into Fall!" % Days_gone)
        elif Days_past < (154+194+178):
            Days_gone = Days_past - (142+194)
            return str("We are %d/178 sols into Winter!" % Days_gone)
        elif Days_past < 669:
            Days_gone = Days_past - (154+194+178)
            return str("We are %d/142 sols into Spring!" % Days_gone)

def Current_Season_EYtoEYCalendar(hemi):
    # calculate current season based on hemisphere, when given Earth year inputs
    if hemi == "Northern":
        season = SeasonCalculatorNh(Mars_Season_at_landing, Days_into_Mars_Season, Difference_in_sols)
        return season
    elif hemi == "Southern":
        season = SeasonCalculatorSh(Mars_Season_at_landing, Days_into_Mars_Season, Difference_in_sols)
        return season

def Current_Season_MYtoMYCalendar(hemi):
    # calculate current season based on hemisphere, when given Mars date inputs
    if hemi == "Northern":
        season = SeasonCalculatorNh(Mars_Season_at_landing, Days_into_Mars_Season, rev_Date_in_sols)
        return season
    elif hemi == "Southern":
        season = SeasonCalculatorSh(Mars_Season_at_landing, Days_into_Mars_Season, rev_Date_in_sols)
        return season

def Give_season(num):
    # convert season number to string for printed output
    if num == 1:
        return "Spring"
    elif num == 2:
        return "Summer"
    elif num == 3:
        return "Autumn"
    elif num == 4:
        return "Winter"

#variables for string output
NowSeason = Current_Season_EYtoEYCalendar(Hemisphere)
Landing_season = Give_season(Mars_Season_at_landing)




# F2: Generate age range for Martian born on Mars -------------------------------------------


#calculate age, lower boundary
Age_range_lower_sols = (Difference_in_MY - MARS_BIRTH_YEAR) * MarsYearInSols
Age_range_lower_days = Age_range_lower_sols*SolInHours/24
Age_range_lower_year = Age_range_lower_days/365.25
Age_lower_year = int(Age_range_lower_year)
Age_lower_days = (Age_range_lower_year - Age_lower_year)*365.25
#calculate age, upper boundary
Age_range_upper_sols = ((Difference_in_MY - MARS_BIRTH_YEAR)+ 0.9999) * MarsYearInSols
Age_range_upper_days = Age_range_upper_sols*SolInHours/24
Age_range_upper_year = Age_range_upper_days/365.25
Age_upper_year = int(Age_range_upper_year)
Age_upper_days = (Age_range_upper_year - Age_upper_year)*365.25





# F3: Mars Year to Earth Year Converter ----------------------------------------



rev_Date_in_sols = Date_to_calculate_MY*MarsYearInSols + Date_to_calculate_sol #gives date in sols
rev_Date_in_Edays = (rev_Date_in_sols*SolInHours/24) + monthConversion(Sol_1_Earth_Year, Sol_1_Earth_Month) + Sol_1_Earth_Date
rev_Date_in_EY = Sol_1_Earth_Year + (rev_Date_in_Edays/365.25)
rev_Date_in_EY_f = int(rev_Date_in_EY) #returns just the year, "floor"
rev_Date_diff = (rev_Date_in_EY - rev_Date_in_EY_f)*365.25 #gives number of days past the new year
#print((rev_Date_in_EY - rev_Date_in_EY_f))
#print(rev_Date_diff)
rev_Season = Current_Season_MYtoMYCalendar(Hemisphere)
#print(rev_Season)



#============================== Printed output

print("\n ============== MISSION CALENDAR LOG ==============") #F1
print("\n Mission landed on sol 1, Earth Date: ", Sol_1_Earth_Year,"/", Sol_1_Earth_Month, "/", Sol_1_Earth_Date)
print(" We landed in the", Hemisphere, "Hemisphere.", "It was", Landing_season, "on Mars.")
print(" As of Earth Date: ", Date_to_calculate_AD, "/", Date_to_calculate_Month, "/", Date_to_calculate_Day, " the date is sol", Difference_in_sols, " or Mars Year ", Difference_in_MY)
print(" A Martian Calendar would say: ", Date_year, " Mars Years + ", Sols_date, " sols")
print("", NowSeason)

print("\n ============== COLONIST INFO ==============") #F2
print("\n Colonist was born in Mars Beta Year: ", MARS_BIRTH_YEAR)
print(" They would be between", Age_lower_year, " Earth Years and ", Age_lower_days, "Earth Days to ", Age_upper_year, " Earth Years and ", Age_upper_days, "Earth Days old.")


print("\n ============== MARS BETA HOMEWORK ASSIGNMENT ============== ") #F3
print("\n Today it is MY", Date_to_calculate_MY, "+", Date_to_calculate_sol,"sols.")
print("", rev_Season)
print(" On Earth, it is the year", rev_Date_in_EY_f, "CE and", rev_Date_diff, "days.")
