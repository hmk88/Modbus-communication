# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 20:16:57 2021

@author: HHAQ
"""

#from pymodbus.payload import Bcd
import tkinter as tk


##########################BCD conversion

def bcd(value, length=0, pad='\x00'):
    ret = ""
    while value:
        value, ls4b = divmod(value, 10)
        value, ms4b = divmod(value, 10)
        ret = chr((ms4b << 4) + ls4b) + ret
    return pad * (length - len(ret)) + ret

################################
    
########################Conversion of BCD into two bytes list 
    
def build(self):
        
        string = str(self)
        length = len(string)
        string = string + ('\x00' * (length % 2))
        return [string[i:i+2] for i in range(0, length, 2)]

#################GUI

window = tk.Tk()
tk.Label(text="Writing MODBUS registers:").pack()
label1 = tk.Label(text="System Password:")
entry1 = tk.Entry(show="*")
label1.pack()
entry1.pack()
system_pass = entry1.get()

label2 = tk.Label(text="Hardware Password:")
entry2 = tk.Entry(show="*")
label2.pack()
entry2.pack()
hardware_pass = entry2.get()

label3 = tk.Label(text="Calendar (date and time): \n (Format: SMHDMY)")
entry3 = tk.Entry()
label3.pack()
entry3.pack()
calendar = entry3.get()

label5 = tk.Label(text="Key to input:")
entry5 = tk.Entry(show="*")
label5.pack()
entry5.pack()
key = entry5.get()

label6 = tk.Label(text="Go to Window #:")
entry6 = tk.Entry()
label6.pack()
entry6.pack()
go_window = entry6.get()

label8 = tk.Label(text="Times for the Beeper: (Max = 255)")
entry8 = tk.Entry()
label8.pack()
entry8.pack()
times_beeper = entry8.get()

label9 = tk.Label(text="Pulses left for OCT: (Max = 65535)")
entry9 = tk.Entry()
label9.pack()
entry9.pack()
pulse = entry9.get()

label4 = tk.Label(text="Day + Hour for Auto-Save: \n(e.g: 0512H means 5th day and 12th hour)")
entry4 = tk.Entry()
label4.pack()
entry4.pack()
day_hour = entry4.get()

label7 = tk.Label(text="LCD Back-lit Lights for number of seconds: (Seconds)")
entry7 = tk.Entry()
label7.pack()
entry7.pack()
lcd = entry7.get()

window.mainloop()

###############################

#############Writing Registers

conv = bcd(system_pass, length=4)
buff = build (conv)
Register_49 = buff[0]
Register_50 = buff[1]

conv = bcd(hardware_pass, length=2)
buff = build (conv)
Register_51 = buff[0]

conv = bcd(calendar, length=6)
buff = build (conv)
Register_53 = buff[0]
Register_54 = buff[1]
Register_55 = buff[2]

conv = bcd(day_hour, length=2)
buff = build (conv)
Register_56 = buff[0]

Register_59 = int(key)

Register_60 = int(go_window)

Register_61 = int(lcd)

Register_62 = int(times_beeper)

Register_63 = int(pulse)
##################################













