import datetime
import calendar
import time;

print("\n")

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

print("\n")

cal = calendar.month(2019, 2)
print ("Here is the calendar:")
print (cal)

print("\n")

currentDT = datetime.datetime.now()

print ("Current Year is: %d" % currentDT.year)
print ("Current Month is: %d" % currentDT.month)
print ("Current Day is: %d" % currentDT.day)
print ("Current Hour is: %d" % currentDT.hour)
print ("Current Minute is: %d" % currentDT.minute)
print ("Current Second is: %d" % currentDT.second)
print ("Current Microsecond is: %d" % currentDT.microsecond)

print("\n")

print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
print (currentDT.strftime("%Y/%m/%d"))
print (currentDT.strftime("%H:%M:%S"))
print (currentDT.strftime("%I:%M:%S %p"))
print (currentDT.strftime("%a, %b %d, %Y"))




