import calendar

print(calendar.calendar(2023))

print(calendar.month(2023,8))

print(calendar.weekday(2023,8,28)) # 0

print(list(calendar.month_name)[1:]) # ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(list(calendar.month_abbr)[1:]) # ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#title 서초구 상점 물건판매량
#x 월
#y 판매량
# 2022년 2023년
# y축 0~140 20단위씩

data = [
    [50, 40, 30, 20, 60, 70, 80, 90, 100, 110, 120, 130],
    [60, 50, 40, 30, 80, 90, 100, 110, 120, 130, 140, 150]
]