from datetime import date

class CalculateAge(object):
    def __init__(self,item):
        self.date = self.Format(item)
    
    def Format(self,item):
        pass

    def AgeById(self):
        pass

    def AgeByDate(self):
        pass

    def Run(self,year,month,day):
        birth = date(year,month,day)
        today = date.today()
        if today <= birth:
            print('Error,你还没出生呢~')
            return
        this_year_birth = birth.replace(year=today.year)      #今年的生日
        next_year_birth = birth.replace(year=today.year + 1)  #明年的生日
        delta_day = (today - this_year_birth).days            #与生日差的天数
        already_day = (today - birth).days                    #已经生活的天数
        # 今年生日还没过
        if delta_day < 0:
            real_old = today.year - birth.year - 1
            next_old_days = abs(delta_day)
        # 今年的生日已经过了
        elif delta_day > 0:
            real_old = today.year - birth.year
            next_old_days = (next_year_birth - today).days
        # 今天是生日（过了今天才算长一岁）
        else:
            real_old = today.year - birth.year - 1
            next_old_days = (next_year_birth - today).days

        print('您现在%d周岁了,距您下一个生日还有%d天,您已经在这个世界生活了%d天.' % (real_old,next_old_days,already_day))
        
a = CalculateAge('2000,1,3')
a.Run(2008,2,29)
