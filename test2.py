import datetime

class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    def show(self):
        print(f"{self.year}/{self.month}/{self.day}")
        
    def add_date(self, date1, date2):
        d1 = datetime.date(date1.year, date1.month, date1.day)
        d2 = datetime.date(date2.year, date2.month, date2.day)
        result_add = d1 + d2
        return result_add
    
while True:
    user_input = int(input("Please Enter 1 For Start Or For Exit Enter Anykey :"))
    if user_input == 1:
        a = int(input("Enter First Year: "))
        b = int(input("Enter First Month: "))
        c = int(input("Enter First Day: "))
        date1 = Date(a, b, c)
        print(date1.show())
        d = int(input("Enter Second Year: "))
        e = int(input("Enter Second Month: "))
        f = int(input("Enter Second Day: "))
        date2 = Date(d, e, f)
        print(date2.show())
        result_s = Date().add_date(date1, date2)
        print(result_s)
    else:
        print("Exiting ...")
        break