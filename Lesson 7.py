import datetime
import os
import shutil

# d = datetime.datetime(2025, 5, 17, 9, 17)
# print(d)
# dn = datetime.datetime.now()
# print(dn)
#
# print(dn.date())
# print(dn.time())
#
# dd = datetime.date(2022,2,24)
# dt = datetime.time(4,31)
#
# d_war = datetime.datetime.combine(dd, dt)
# print(d_war)
#
# d_war = d_war.replace(year=2025)
# print(d_war)
#
# print(dn.weekday())
# print(dn.isoweekday())


# path = 'C:\\Users\\gololobov\\Downloads\\Logo\\Python.jpg'
# f = os.path.getctime(path)
#
# d = datetime.datetime.fromtimestamp(f)
# print(d)
#
# print(d.strftime("%d.%m.%Y %H:%M, %A"))
# print(d.strftime("%d %B %Y, %H:%M, %A"))
#
# print(datetime.datetime.now() - d)
#
# td = datetime.timedelta(seconds=2147483647)
# dp = datetime.datetime(1970,1,1)
# print(dp+td)

path = 'C:\\Users\\gololobov\\Downloads\\Logo\\'
res_path = 'C:\\Users\\gololobov\\Downloads\\Logo\\Test'

def spy2(path, res_path):
    path = os.path.normpath(path)
    res_path = os.path.normpath(res_path)
    for path, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_date = os.path.getctime(f"{path}\\{file}")
            norm_date = datetime.datetime.fromtimestamp(file_date)
            str_date = norm_date.strftime("%d.%m.%Y")

            if not os.path.isdir(f"{res_path}\\{str_date}"):
                os.mkdir(f"{res_path}\\{str_date}")
            shutil.copy(f"{path}\\{file}", f"{res_path}\\{str_date}\\{file}")

spy2(path, res_path)