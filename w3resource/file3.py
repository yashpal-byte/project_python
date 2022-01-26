#3. Write a Python program to display the current date and time.
import datetime
date_obj = datetime.datetime.now()
print(date_obj.strftime("%y-%m-%d %H:%M:%S"))