from datetime import datetime

my_date_string = "July 22 2023 04:35PM"

datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)