"""
逝去的青葱年华 :)
"""
from datetime import date
import logging
import sys
import time
import math


# logging.basicConfig(
#     filename="log",
#     level=logging.INFO,
#     format="%(asctime)s:%(levelname)s:%(message)s"
# )

class DateCal:
    """
    计算从出生到现在生活的时间段, 结果用: 年+日+%H%M%S 表示
    """
    def __init__(self):
        self.argvList = sys.argv
        self.bYear = self.argvList[1]
        self.bMonth = self.argvList[2]
        self.bDay = self.argvList[3]
        self.expectYear = int(self.argvList[4])
        if int(self.bMonth) < 10:
            self.bMonth = "0"+self.bMonth
        if int(self.bDay) < 10:
            self.bDay = "0"+self.bDay

    
    def cal(self):
        # year = date.today().year
        # month = date.today().month
        # day = date.today().day
        # year = str(year)
        # if month < 10:
        #     month = "0" + str(month)
        # else:
        #     month = str(month)
        # if day < 10:
        #     day = "0" + str(day)
        # else:
        #     day = str(day)
        # a = int(year+month+day)
        # b = int(self.bYear+self.bMonth+self.bDay)
        # if  a < b:
        #     logging.info("年月日格式出错, 请检查!")
        # else:
        #     if int(month+day) < int(self.bMonth+self.bDay):
        #         subDay = date(int(year), int(month), int(day)) - date(int(year)-1, int(self.bMonth), int(self.bDay))
        #         subYear = str(int(year)-1 - int(self.bYear))
        #         print("你已经生活在这个地球上: {}年, {}天".format(subYear, subDay.days))
        #     else:
        #         subDay = date(int(year), int(month), int(day)) - date(int(year), int(self.bMonth), int(self.bDay))
        #         subYear = int(year) - int(self.bYear)
        #         print("你已经生活在这个地球上: {}年, {}天".format(subYear, subDay.days))
        born_date = "{}-{}-{}-12-00-00".format(self.bYear, self.bMonth, self.bDay)
        bs = time.strptime(born_date, "%Y-%m-%d-%H-%M-%S")
        born_timestamp = time.mktime(bs)
        now = math.floor(time.time())
        subsSeconds = math.floor(now - born_timestamp)
        oneYearSeconds = 365*24*3600 + 5*3600 + 48*60
        pYear = subsSeconds//oneYearSeconds
        remainder = subsSeconds - (pYear*oneYearSeconds)
        pDay = remainder//(24*3600)
        remainder = remainder - pDay*(24*3600)
        pHour = remainder//3600
        remainder = remainder - pHour*3600
        pMimute = remainder//60
        pSecond = remainder%60
        print("你生活在这个地球上: {}年{}天{}时{}分{}秒".format(pYear, pDay, pHour, pMimute, pSecond))

        expectSeconds = self.expectYear*oneYearSeconds
        progress = str(((subsSeconds/expectSeconds)*100).__round__(2))+"%"
        print("你期望生活{}年, 已经度过{}".format(self.expectYear, progress))

if __name__ == "__main__":
    d = DateCal()
    d.cal()
