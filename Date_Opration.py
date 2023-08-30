#Dates Opration
print("                                  Welcome                                ")
print("                         Dates Opration Application                      ")
print("                                  By Jey                                 ")
class Date:
    def __init__(self, year, month, day):                # یک کلاس به نام تاریخ که دارای سه مولفه سال ماه و روز میشود درست شده است.
        self.year = year
        self.month = month
        self.day = day                                   #سلف مشخص میکند که این مولفه ها برای تمامی کلاس شناخته شده باشند
    
    def __str__(self):                                   #با این فانکشن فونت دیکشنری ما بصورت صحیح  چاپ میشود.
        print(f"Your Result Dates Is :{self.year}/{self.month}/{self.day}")
         
##############################################################################
    def month_name(self):
        month_name = ['Farvardin', 'Odibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar', 'Mehr', 'Aban', 'Azar', 'Dey', 'Bahman', 'Esfand']#ماه های سال در یک لیست
        return month_name[self.month -1]                 #در این خط شماره سلف مانس بدلیل فرمت لیستی خود منهای یک میشود تا مانس نیم عدد مورد نظر را برگرداند.
                     #Examp :[2-1]=1 Odibehesht (Indext Numbers = 0 1 2 3 4 5 6 ...)
    def add_dates(self, self_day2): 
        new_day = self.day +self_day2.day                # مقادیر روزها در تاریخ خط 76 و 77
        new_month = self.month + self_day2.month         # مقادیر ماه ها در تاریخ خط 76 و 77
        new_year = self.year + self_day2.year            # مقادیر سال ها در تاریخ خط 76 و 77

        if new_day>30:                                   #اگر مقدار تعداد روز ها از 30 بیشتر شد
            new_day-=30                                  #مجدد ان را صفر کن یعنی 30 تا ازش کم کن
            new_month+=1                                 #و بعد از آن یک عدد به مقدار ماه اضافه کن
            
        if new_month>12:                                 #اگر مقدار تعداد ماه ها از 12 بیشتر شد
           new_month-=12                                 #مجدد آن را صفر کن یعنی 12 تا ازش کم کن
           new_year+=1                                   #و بعد از آن بک عدد به مقدار سال اضافه کن
         
        return Date(new_year, new_month,  new_day)       #مقادیر جدید به  کلاس تاریخ برگردانده میشوند
    
    def substract(self, another_date2):                  #این فانکشن نیز همانند فانکشن جمع عملکرد مشابهی دارد ولی فقط اینبارعملگر تفریق
        day_sub = self.day - another_date2.day
        month_sub = self.month - another_date2.month
        year_sub = self.year - another_date2.year
        
        if day_sub<0:
            day_sub+=30
            month_sub-=1
            
        if month_sub<0:
            month_sub+=12
            year_sub-=1
               
        return Date(year_sub, month_sub,day_sub)

    def isvalidDate(self):                                # چک کردن اعتبار
        if self.year not in range(1 , 9999):              # اگر مقدار سال بین 1 تا 9999 نبود
            return False                                  # print false  بگو غلطه
        
        elif self.month not in range (1 , 12):            #اگر مقدار ماه بین 1 تا 12 نبود
            return False                                  #print false بگو غلطه
        
        elif self.day not in range(1 , 30):               #اگر روز بین 1 تا 30 نبود
            return False                                  #print false بگو غلطه
       
        else:                                             # وگرنه 
            return True                                   #print True  بگو درسته
            
#########################################################################
#Main_Loop
while True:
    user_input=(input("For Start Type 1 And For Exit Type anykey:"))  #برای شروع عدد یک وارد شود برای خروج از برنامه هرکلیدی که مایلدید وارد کنید . 
    if user_input=="1":                                               #عدد یک بصورت استرینگ تعریف شده است چون هرعددی توی ورود کاربر رشته میباشد .
        print("Enter Year , Month And Day that u want Oprate! :")
        a = int(input('Enter  1th  Year ='))
        b = int(input('Enter  1th  Month ='))
        c = int(input('Enter  1th  Day ='))
        print(f"Your First Date Is :{a}/{b}/{c}")                     # اولین تاریخ ورودی توسط کاربر
        d = int(input('Enter  2th  Year ='))
        e = int(input('Enter  2th  Month ='))
        f = int(input('Enter  2th  Day ='))
        print(f"Your Second Date Is :{d}/{e}/{f}")                    #دومین تاریخ ورودی توسط کاربر
        date1 = Date(a, b, c)                                         # این خط برای ساختن دو تاریخ با استفاده از سه عدد سال و ماه و روز می باشد .
        date2 = Date(d, e, f)
        for i in range(4):
            User_Choice = (input('If u Want To add Type 1 elif Sub Type 2 elif Month Name Type 3  elif IsvalidDate Type 4 else Type Anykey :'))             #درخواست از کاربر برای انتخاب عملیات
            if User_Choice=="1":
                result_add= date1.add_dates(date2)                    #در این خط تابع عملیات جمع از کلاس ! دو تاریخ را به هم برای انجام عملیات مرتبط میکند.
                result_add.__str__()                                  #  فراخونی برای چاپ
            
            elif User_Choice=="2":
                result_substract= date1.substract(date2)              #در این خط تابع عملیات تفریق از کلاس ! دو تاریخ را به هم برای انجام عملیات مرتبط میکن
                result_substract.__str__()                            #  فراخونی برای چاپ
            

            elif User_Choice=="3":
                month_name1= date1.month_name()                       #فراخوانی فانکشن گرفتن نام و ایندکس  ماه تاریخ اول
                month_name2= date2.month_name()                       #فراخوانی فانکشن گرفتن نام و ایندکس  ماه تاریخ دوم
                print(f'Month_name1: {month_name1}')                  #چاپ نام ماه مورد نظر از تاریخ اول
                print(f'Month_name2: {month_name2}')                  #چاپ نام ماه مورد نظر از تاریخ دوم


            elif User_Choice=="4":
                validdate1=date1.isvalidDate()                        #فرخوانی فانکشن اعتبار و چک کردن سال اول
                validdate2=date2.isvalidDate()                        #فراخوانی فانکشن اعتبار و چک کردن سال دوم
             
                print(f"Year1 Is Valid? {validdate1}")                #چاپ نهایی
                print(f"Year2 Is Valid? {validdate2}")
            else:
                print("Wrong input...")
                print("Try Again...")
                
            
                        
    else:
        print("Exiting ...") #در حال خروج
        break