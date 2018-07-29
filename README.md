# MartianCalendar

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
Not for professional purposes. Code author created this to have accurate world building for a sci-fi novel. If anyone
likes to read sci-fi novels about the doom of a Mars colony and extreme human suffering hit me up!
NB: I 100% support Mars and space exploration and think it's the direction people should be taking and think it will be successful and beneficial to humanity. I just like scary books. """


__author__ = "Diane Magnin"
__version__ = "1.3"
__email__ = "dianemagnin@yahoo.com"
__twitter__ = "@DianeM97"
