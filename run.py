from os import sep
from posixpath import split
import datetime
from datetime import timedelta
from datetime import datetime
from datetime import time
import re
import os.path
import sys



import calendar
# test_num = 3
# res = calendar.month_name[test_num]
# print("Month Name from Number : " + str(res))


# def mn(mnp):
#     # res = calendar.month_name[mnp]        #for full name
#     res = calendar.month_abbr[mnp]
#     return res
# print(mn(2))

def mc(sm):
    return {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '010',
        'Nov': '011',
        'Dec': '012',
        'jan': '1',
        'feb': '2',
        'mar': '3',
        'apr': '4',
        'may': '5',
        'jun': '6',
        'jul': '7',
        'aug': '8',
        'sep': '9',
        'oct': '10',
        'nov': '11',
        'dec': '12'
    }[sm]


def std(stime):
    # wihtout it show random date also
    datetimepbj = datetime.strptime(stime, '%H:%M')
    return datetimepbj


now = datetime.now()
nowY = now.strftime("%Y")

dlog = datetime.now().strftime("%Y%m%d-%H%M%S")
dext = ".txt"
# logf = str(dlog+dext)
logf = dlog+dext

if os.path.exists(os.path.join(sys.path[0],"data2")):
    os.remove(os.path.join(sys.path[0],"data2"))
    with open(os.path.join(sys.path[0],"data.txt"), "r") as data:
        for line in data.readlines():
            if ((not line.startswith("ramneet")) & (not line.__contains__("lele")) & (not line.endswith("saini"))):

                # for line in data.readlines():
                # x = re.findall("ssss", line)
                # if not x:
                itm = timedelta(minutes=2)
                with open(os.path.join(sys.path[0],"data2"), "a+") as data2:
                    print(line.split()[0], nowY+"-"+mc(line.split()[5])+"-" +
                          line.split()[6], line.split()[7], (std(line.split()[9])+itm).strftime("%H:%M"), file=data2)
                data2.close
    data.close

    with open(os.path.join(sys.path[0],"data2"), "r") as data2p:
        for var in data2p:
            uname = var.split()[0]
            date = var.split()[1]
            tin = var.split()[2]
            tou = var.split()[3]
            with open(os.path.join(sys.path[0],logf), "a+") as l:
                print("Hi user name is ", uname, "date is ", date,
                      "time in ", tin, "time out is ", tou, file=l)
            l.close
    data2p.close

else:
    with open(os.path.join(sys.path[0],"data.txt"), "r") as data:
        for line in data.readlines():
            if ((not line.startswith("ramneet")) & (not line.__contains__("lele")) & (not line.endswith("saini"))):

                # for line in data.readlines():
                # x = re.findall("ssss", line)
                # if not x:
                itm = timedelta(minutes=2)
                with open(os.path.join(sys.path[0],"data2"), "a+") as data2:
                    print(line.split()[0], nowY+"-"+mc(line.split()[5])+"-" +
                          line.split()[6], line.split()[7], (std(line.split()[9])+itm).strftime("%H:%M"), file=data2)
                data2.close
    data.close

    with open(os.path.join(sys.path[0],"data2"), "r") as data2p:
        for var in data2p:
            uname = var.split()[0]
            date = var.split()[1]
            tin = var.split()[2]
            tou = var.split()[3]
            with open(os.path.join(sys.path[0],logf), "a+") as l:
                print("Hi user name is ", uname, "date is ", date,
                      "time in ", tin, "time out is ", tou, file=l)
            l.close
    data2p.close()
