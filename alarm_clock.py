import datetime
import time
import os

weekdays = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
day = datetime.datetime.now()
t = time.strftime("%H:%M")
tone = 'chime.mp3'

if day.strftime('%a') in weekdays:
    if t == '16:24':
        while t == '16:25':
            print('Wake Up!')
            os.system('vlc ' + tone)