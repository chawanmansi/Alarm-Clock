# importing the required lib         
from tkinter import *  
import datetime as dt  
import time
import winsound as ws
  
# defining the function for the alarm clock  
def alarm(setAlarmTimer):  
    while True:  
        time.sleep(1)
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S")  
        currentDate = actualTime.strftime("%d / %m / %Y")  
        the_message = "Current Time: " + str(currentTime)  
        print(the_message)  
        if currentTime == setAlarmTimer:  
            ws.PlaySound("sound.wav", ws.SND_ASYNC)  
            break  
  
def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmSetTime)  
  
# creating the GUI for the application  
guiWindow = Tk()  
guiWindow.title("The Alarm Clock")  
guiWindow.geometry("464x230")  
guiWindow.config(bg = "#03A89E")  
guiWindow.resizable(width = False, height = False)  
   
timeFormat = Label(  
    guiWindow,  
    text = "Enter time in 24 hour format!",  
    fg = "#000080",  
    bg = "#C71585",  
    font = ("Arial", 15)  
    ).place(  
        x = 100, 
        y = 170  
        )  
   
add_time = Label(  
    guiWindow,  
    text = "Hour      Minute    Second",  
    font = ("Arial", 11, "bold")  ,
    fg = "#F5F5F5",  
    bg = "#03A89E"  
    ).place(  
        x = 230,  
        y = 10  
        )  
  
setAlarm = Label(  
    guiWindow,  
    text = "Set Time for Alarm: ",  
    fg = "white",  
    bg = "#006400",  
    relief = "solid",  
    font = ("Helevetica", 13, "bold")  
    ).place(  
        x = 13,  
        y = 53  
        )  
   
hour = StringVar()  
minute = StringVar()  
second = StringVar()  
   
hourTime = Entry(  
    guiWindow,  
    textvariable = hour,  
    bg = "lightpink2",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 230,  
        y = 53  
        )  
minuteTime = Entry(  
    guiWindow,  
    textvariable = minute,  
    bg = "lightpink2",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 297,  
        y = 53  
        )  
secondTime = Entry(  
    guiWindow,  
    textvariable = second,  
    bg = "lightpink2",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 365,  
        y = 53  
        )  
   
submit = Button(  
    guiWindow,  
    text = "Set The Alarm",  
    fg = "white",  
    bg = "#008080",  
    width = 15,  
    command = getAlarmTime,  
    font = (20)  
    ).place(  
        x = 160,  
        y = 110  
        )  
   
guiWindow.mainloop()  