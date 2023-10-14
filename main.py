"""
A demo for the app: JustCareTrakr
"""
from HealthData import HealthData as hd
import matplotlib.pyplot as plt
from healthuser import HealthUser
import random


def how_diet(response: str) -> int:  # Place holder for a language model like GPT 4
    points = 0
    if response == "great":
        points = 5
    elif response == "good":
        points = 3
    elif response == "bad":
        points = 2
    elif response == "terrible":
        points = 1
    else:
        points = -1
    return points


# Place holder function for a language model to discern the users feelings towards their progress
def how_exercise(response: str) -> int:
    points = 0
    if response == "great":
        points = 5
    elif response == "good":
        points = 3
    elif response == "bad":
        points = 2
    elif response == "terrible":
        points = 1
    else:
        points = -1
    return points


# registered a user to transition to a better diet
p0 = HealthUser("Edward", 23, 100, 10, 0, 10)
# registered a user for a change in exercise process
p1 = HealthUser("Diego", 24, 100, 5, 10, 10)
# registered a user for a slight increase in over all lifestyle to lose weight
p2 = HealthUser("Ethan", 21, 120, 10, 10, 10)

# day 0 *users that have registered at different times are to be accounted for in the production version
user = {
    'Sleep': 0,
    'Diet': 0,
    'Exercise': 0
}

dfp0 = hd(user)
dfp1 = hd(user)
dfp2 = hd(user)

#  day 1
p0.set_diet(3)
p0.set_exercise(5)
p0.set_sleep(5)

p1.set_diet(-1)
p1.set_exercise(0)
p1.set_sleep(4)

p2.set_diet(0)
p2.set_exercise(0)
p2.set_sleep(0)

day1 = [p0.get_sleep(), p0.get_diet(), p0.get_exercise()]
dfp0.add(day1)

day1 = [p1.get_sleep(), p1.get_diet(), p1.get_exercise()]
dfp1.add(day1)

day1 = [p2.get_sleep(), p2.get_diet(), p2.get_exercise()]
dfp2.add(day1)

#  day 2
p0.set_diet(1)
p0.set_exercise(3)
p0.set_sleep(3)

p1.set_diet(3)
p1.set_exercise(2)
p1.set_sleep(5)

p2.set_diet(-1)
p2.set_exercise(2)
p2.set_sleep(5)

day1 = [p0.get_sleep(), p0.get_diet(), p0.get_exercise()]
dfp0.add(day1)

day1 = [p1.get_sleep(), p1.get_diet(), p1.get_exercise()]
dfp1.add(day1)

day1 = [p2.get_sleep(), p2.get_diet(), p2.get_exercise()]
dfp2.add(day1)


# day 3
p0.set_diet(5)
p0.set_exercise(-1)
p0.set_sleep(5)

p1.set_diet(1)
p1.set_exercise(0)
p1.set_sleep(4)

p2.set_diet(5)
p2.set_exercise(5)
p2.set_sleep(5)

day1 = [p0.get_sleep(), p0.get_diet(), p0.get_exercise()]
dfp0.add(day1)

day1 = [p1.get_sleep(), p1.get_diet(), p1.get_exercise()]
dfp1.add(day1)

day1 = [p2.get_sleep(), p2.get_diet(), p2.get_exercise()]
dfp2.add(day1)


# day 4
p0.set_diet(5)
p0.set_exercise(3)
p0.set_sleep(-1)

p1.set_diet(2)
p1.set_exercise(-1)
p1.set_sleep(-2)

p2.set_diet(3)
p2.set_exercise(2)
p2.set_sleep(1)

day1 = [p0.get_sleep(), p0.get_diet(), p0.get_exercise()]
dfp0.add(day1)

day1 = [p1.get_sleep(), p1.get_diet(), p1.get_exercise()]
dfp1.add(day1)

day1 = [p2.get_sleep(), p2.get_diet(), p2.get_exercise()]
dfp2.add(day1)

# day 5
p0.set_diet(-1)
p0.set_exercise(2)
p0.set_sleep(2)

p1.set_diet(-1)
p1.set_exercise(0)
p1.set_sleep(4)

p2.set_diet(0)
p2.set_exercise(0)
p2.set_sleep(0)

day1 = [p0.get_sleep(), p0.get_diet(), p0.get_exercise()]
dfp0.add(day1)

day1 = [p1.get_sleep(), p1.get_diet(), p1.get_exercise()]
dfp1.add(day1)

day1 = [p2.get_sleep(), p2.get_diet(), p2.get_exercise()]
dfp2.add(day1)


# day 6
p0.set_diet(5)
p0.set_exercise(2)
p0.set_sleep(1)

p1.set_diet(0)
p1.set_exercise(0)
p1.set_sleep(0)

p2.set_diet(0)
p2.set_exercise(0)
p2.set_sleep(0)

day1 = [p0.get_sleep(), p0.get_diet(), p0.get_exercise()]
dfp0.add(day1)

day1 = [p1.get_sleep(), p1.get_diet(), p1.get_exercise()]
dfp1.add(day1)

day1 = [p2.get_sleep(), p2.get_diet(), p2.get_exercise()]
dfp2.add(day1)


# day 7
p0.set_diet(1)
p0.set_exercise(5)
p0.set_sleep(3)

p1.set_diet(5)
p1.set_exercise(4)
p1.set_sleep(4)

p2.set_diet(-1)
p2.set_exercise(-1)
p2.set_sleep(-1)

day1 = [p0.get_sleep(), p0.get_diet(), p0.get_exercise()]
dfp0.add(day1)

day1 = [p1.get_sleep(), p1.get_diet(), p1.get_exercise()]
dfp1.add(day1)

day1 = [p2.get_sleep(), p2.get_diet(), p2.get_exercise()]
dfp2.add(day1)


####################################################################
# Edward
x1_values = list(range(len(dfp0.getCol('Sleep'))))
y1_values = dfp0.getCol('Sleep')

x2_values = list(range(len(dfp0.getCol('Diet'))))
y2_values = dfp0.getCol('Diet')

x3_values = list(range(len(dfp0.getCol('Exercise'))))
y3_values = dfp0.getCol('Exercise')


fig, ax = plt.subplots()

# Plot the first line
ax.plot(x1_values, y1_values, label='Sleep')

# Plot the second line
ax.plot(x2_values, y2_values, label='Diet')

# Plot the second line
ax.plot(x3_values, y3_values, label='Exercise')


plt.xlabel('Days')
plt.ylabel('Progress')
plt.title(str(p0))

plt.legend()


####################################################################
# Diego
x1_values = list(range(len(dfp1.getCol('Sleep'))))
y1_values = dfp1.getCol('Sleep')

x2_values = list(range(len(dfp1.getCol('Diet'))))
y2_values = dfp1.getCol('Diet')

x3_values = list(range(len(dfp1.getCol('Exercise'))))
y3_values = dfp1.getCol('Exercise')


fig, ax = plt.subplots()

# Plot the first line
ax.plot(x1_values, y1_values, label='Sleep')

# Plot the second line
ax.plot(x2_values, y2_values, label='Diet')

# Plot the second line
ax.plot(x3_values, y3_values, label='Exercise')


plt.xlabel('Days')
plt.ylabel('Progress')
plt.title(str(p1))

plt.legend()


####################################################################
# Ethan
x1_values = list(range(len(dfp2.getCol('Sleep'))))
y1_values = dfp2.getCol('Sleep')

x2_values = list(range(len(dfp2.getCol('Diet'))))
y2_values = dfp2.getCol('Diet')

x3_values = list(range(len(dfp2.getCol('Exercise'))))
y3_values = dfp2.getCol('Exercise')


fig, ax = plt.subplots()

# Plot the first line
ax.plot(x1_values, y1_values, label='Sleep')

# Plot the second line
ax.plot(x2_values, y2_values, label='Diet')

# Plot the second line
ax.plot(x3_values, y3_values, label='Exercise')


plt.xlabel('Days')
plt.ylabel('Progress')
plt.title(str(p2))

plt.legend()
plt.show()
