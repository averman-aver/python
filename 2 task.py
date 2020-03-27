time_sec = int(input('время в секундах: '))
hour = time_sec//3600
minute = (time_sec%3600)//60 # - hour * 60)
sec = (time_sec%3600)%60
print(hour, minute, sec, sep = ':')