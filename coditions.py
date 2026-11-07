#weather repoter

city= input("Enter your city:")
temp= float(input("Enter today's temperature in C:"))

if temp>35:
    print("Warning: it is very hot today.")

if temp>25:
    print("Great day to go ountside!")
else:
    print("Grab a jacket before you go out.")

if temp>35:
    print("Weather: Scorching Hot")
elif temp>25:
    print("Weather: Warm amd Sunny")
elif temp>15:
    print("Weather: Cooland Breazy")
else:
    print("Weather: Cold - stay warm!")

import datetime
import calendar

now= datetime.datetime.now()
print("City:", city)
print("TIme now:", now)

print(calendar.calendar(now.year))
