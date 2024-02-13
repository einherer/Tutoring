from datetime import datetime

print("Now at the moment", datetime.now())

wish_date = datetime(2024, 2, 14, 18)   #ommiting minutes and sekondes results in 00:00
print("Valentine's Dinner", wish_date)

date_as_str = "2024, 2, 14, 18"

print(date_as_str)
parsed_date = datetime.strptime(date_as_str, "%Y, %m, %d, %H")
print(parsed_date)

print(parsed_date.strftime("%d.%m.%y"))
print(parsed_date.strftime("%Y%m%d%H%M%S"), "what ever happend and needs to be logged")

print(parsed_date.time())

print(wish_date - datetime.now())   # time untill the date has come