#Câu 2: Tính giờ phút giây
'''
Nhập vào số giây bất kỳ t. Tính và xuất ra dạng
Giờ:Phút:Giây
Ví dụ: Nhập 3750 thì xuất ra 1:2:30 AM
Nhập 51100 thì xuất ra 2:11:40 PM
HD:
hour=(t/3600)%24
minute=(t%3600)/60
second=(t%3600)%60  
'''
t = int(input("Nhập số giây: "))

hour = (t // 3600) % 24
minute = (t % 3600) // 60
second = (t % 3600) % 60

if hour == 0:
    display_hour = 12
    period = "AM"
elif 1 <= hour < 12:
    display_hour = hour
    period = "AM"
elif hour == 12:
    display_hour = 12
    period = "PM"
else:
    display_hour = hour - 12
    period = "PM"

print(f"{display_hour}:{minute:02}:{second:02} {period}")


