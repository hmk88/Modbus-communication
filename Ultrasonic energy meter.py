# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:08:54 2021

Modbus data conversion and presentation
@author: HHAQ
"""

#   Module imports

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
import tkinter as tk


########################   Importing Ultrasonic flow meter file 

def flowMeter(file):
    fileObj = open(file, "r") #Opening the file
    Array = fileObj.read().splitlines() #Saving each lines in an array
    fileObj.close() #Cloding the file
    Array = list(map(int,Array))    #Converting the array into integer
    return Array

########################

#######################   Decoding REAL 4 format

def realFour(a, b):
    registers = [a, b]
    decoder = BinaryPayloadDecoder.fromRegisters(registers, byteorder=Endian.Big)
    c= decoder.decode_32bit_float() 
    c=float("{:.4f}".format(c))
    return c 

#######################

#######################   Decoding LONG format

def long(i, j):
    registers = [i, j]
    decoder = BinaryPayloadDecoder.fromRegisters(registers, byteorder=Endian.Big)
    k= decoder.decode_32bit_int()
    return k 

#######################

#######################   Decoding INTEGER format

def inte(l):
    registers = [l]
    decoder = BinaryPayloadDecoder.fromRegisters(registers, byteorder=Endian.Big)
    o= decoder.decode_16bit_int()  
    return o 

#######################



########################################    Main
    
file = "C:\\Users\\hhaq\\Documents\\Gambit\\energy_meter_preprocess.txt"
Array = flowMeter(file) 

#   Extraction and decoding register values

flowrate = realFour(Array[1], Array[0]) #   Higher register first, lower register second
flowrate 

energy_flowrate = realFour(Array[3], Array[2])  #   Higher register first, lower register second
energy_flowrate

velocity = realFour(Array[4], Array[5])  #   Lower register first, higher register second
velocity

fluid_soundspeed = realFour(Array[7], Array[6])  #   Lower register first, higher register second
fluid_soundspeed

positive_accumulator = long(Array[8], Array[9])  #   Lower register first, higher register second
positive_accumulator            #Gallon 

positive_decimalfraction = realFour(Array[11], Array[10])  #   Lower register first, higher register second
positive_decimalfraction        #Gallon

negative_accumulator = long(Array[13], Array[12])  #   Lower register first, higher register second
negative_accumulator

negative_decimalfraction = realFour(Array[15], Array[14])  #   Lower register first, higher register second
negative_decimalfraction

positive_energyaccumulator =long(Array[17], Array[16])  #   Lower register first, higher register second
positive_energyaccumulator

positive_energy_decimalfraction = realFour(Array[19], Array[18])  #   Lower register first, higher register second
positive_energy_decimalfraction

negative_energyaccumulator =long(Array[21], Array[20])  #   Lower register first, higher register second
negative_energyaccumulator

negative_energy_decimalfraction = realFour(Array[23], Array[22])  #   Lower register first, higher register second
negative_energy_decimalfraction

net_accumulator = long(Array[25], Array[24])  #   Lower register first, higher register second
net_accumulator

net_decimalfraction = realFour(Array[27], Array[26])  #   Lower register first, higher register second
net_decimalfraction

net_energyaccumulator = long(Array[29], Array[28])  #   Lower register first, higher register second
net_energyaccumulator

net_energy_decimalfraction = realFour(Array[31], Array[30])  #   Lower register first, higher register second
net_energy_decimalfraction

temperature_inlet = realFour(Array[33], Array[32])  #   Lower register first, higher register second
temperature_inlet

temperature_outlet = realFour(Array[35], Array[34])  #   Lower register first, higher register second
temperature_outlet

analog_in_ai3 = realFour(Array[37], Array[36])  #   Lower register first, higher register second
analog_in_ai3

analog_in_ai4 = realFour(Array[39], Array[38])  #   Lower register first, higher register second
analog_in_ai4

analog_in_ai5 = realFour(Array[41], Array[40])  #   Lower register first, higher register second
analog_in_ai5

current_in_ai3 = realFour(Array[43], Array[42])  #   Lower register first, higher register second
current_in_ai3

current_in_ai4 = realFour(Array[45], Array[44])  #   Lower register first, higher register second
current_in_ai4

current_in_ai5 = realFour(Array[47], Array[46])  #   Lower register first, higher register second
current_in_ai5

resistance_in = realFour(Array[77], Array[76])  #   Lower register first, higher register second
resistance_in

resistance_out = realFour(Array[79], Array[78])  #   Lower register first, higher register second
resistance_out

total_travel_time = realFour(Array[81], Array[80])  #   Lower register first, higher register second
total_travel_time 

delta_travel_time = realFour(Array[83], Array[82])  #   Lower register first, higher register second
delta_travel_time

upstream_travel_time = realFour(Array[85], Array[84])  #   Lower register first, higher register second
upstream_travel_time

downstream_travel_time = realFour(Array[87], Array[86])  #   Lower register first, higher register second
downstream_travel_time

output_current = realFour(Array[89], Array[88])  #   Lower register first, higher register second
output_current

signal_quality = inte(Array[91])  
signal_quality = int (signal_quality/10)
signal_quality

upstream_strength = inte(Array[92])  
upstream_strength

downstream_strength = inte(Array[93])  
downstream_strength

if Array[95] == 0:
    language_used = "English"
else:
    language_used ="Chinese"
    
language_used

rate_travel_time = realFour(Array[97], Array[96])  #   Lower register first, higher register second
rate_travel_time

reynolds_number = realFour(Array[99], Array[98])  #   Lower register first, higher register second
reynolds_number




#############################GUI
window = tk.Tk()

frame0 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame0.grid(row=1, column=1)
frame00 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame00.grid(row=1, column=2)
frame000 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame000.grid(row=1, column=3)
frame0000 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame0000.grid(row=1, column=4)
frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame1.grid(row=2, column=1)
frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame2.grid(row=2, column=2)
frame3 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame3.grid(row=2, column=3)
frame4 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame4.grid(row=2, column=4)
frame5 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame5.grid(row=3, column=1)
frame6 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame6.grid(row=3, column=2)
frame7 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame7.grid(row=3, column=3)
frame8 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame8.grid(row=3, column=4)
frame9 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame9.grid(row=4, column=1)

tk.Label(master=frame0,text="Ultrsonic flow meter reading:").pack()
tk.Label(master=frame00,text="Date: 2018-08-03 04:06").pack()
tk.Label(master=frame000,text=f"Signal Quality: {signal_quality} (Range: 0-99)").pack()
tk.Label(master=frame0000,text=f"Language Used in Interface: {language_used}").pack()
tk.Label(master=frame1,text=f"Flow Rate: {flowrate} (m3/h)").pack()
tk.Label(master=frame1,text=f"Energy Flow Rate: {energy_flowrate} (GJ/h)").pack()
tk.Label(master=frame1,text=f"Velocity: {velocity} (m/s)").pack()
tk.Label(master=frame1,text=f"Fluid Sound Speed: {fluid_soundspeed} (m/s)").pack()
tk.Label(master=frame2,text=f"Positive Accumulator: {positive_accumulator} (Gallon)").pack()
tk.Label(master=frame2,text=f"Positive Decimal Fraction: {positive_decimalfraction} (Gallon)").pack()
tk.Label(master=frame2,text=f"Negative Accumulator: {negative_accumulator}").pack()
tk.Label(master=frame2,text=f"Negative Decimal Fraction: {negative_decimalfraction}").pack()
tk.Label(master=frame3,text=f"Positive Energy Accumulator: {positive_energyaccumulator}").pack()
tk.Label(master=frame3,text=f"Positive Energy Decimal Fraction: {positive_energy_decimalfraction}").pack()
tk.Label(master=frame3,text=f"Negative Energy Accumulator: {negative_energyaccumulator}").pack()
tk.Label(master=frame3,text=f"Negative Energy Decimal Fraction: {negative_energy_decimalfraction}").pack()
tk.Label(master=frame4,text=f"Net Accumulator: {net_accumulator}").pack()
tk.Label(master=frame4,text=f"Net Decimal Fraction: {net_decimalfraction}").pack()
tk.Label(master=frame4,text=f"Net Energy Accumulator: {net_energyaccumulator}").pack()
tk.Label(master=frame4,text=f"Net Energy Decimal Fraction: {net_energy_decimalfraction}").pack()
tk.Label(master=frame5,text=f"Temperature # 1 (Inlet): {temperature_inlet} (degC)").pack()
tk.Label(master=frame5,text=f"Temperature # 2 (Outlet): {temperature_outlet} (degC)").pack()
tk.Label(master=frame5,text=f"Analog Input AI3: {analog_in_ai3}").pack()
tk.Label(master=frame5,text=f"Analog Input AI4: {analog_in_ai4}").pack()
tk.Label(master=frame6,text=f"Analog Input AI5: {analog_in_ai5}").pack()
tk.Label(master=frame6,text=f"Current Input at AI3: {current_in_ai3} (mA)").pack()
tk.Label(master=frame6,text=f"Current Input at AI4: {current_in_ai4} (mA)").pack()
tk.Label(master=frame6,text=f"Current Input at AI5: {current_in_ai5} (mA)").pack()
tk.Label(master=frame7,text=f"PT100 Resistance of inlet: {resistance_in} (Ohm)").pack()
tk.Label(master=frame7,text=f"PT100 Resistance of Outlet: {resistance_out} (Ohm)").pack()
tk.Label(master=frame7,text=f"Total Travel Time: {total_travel_time} (Micro Second").pack()
tk.Label(master=frame7,text=f"Delta Travel Time: {delta_travel_time} (Micro Second").pack()
tk.Label(master=frame8,text=f"Upstream Travel Time: {upstream_travel_time} (Micro Second").pack()
tk.Label(master=frame8,text=f"Downstream Travel Time: {downstream_travel_time} (Micro Second)").pack()
tk.Label(master=frame8,text=f"Output Current: {output_current} (mA)").pack()
tk.Label(master=frame8,text=f"Upstream Strength: {upstream_strength} (Range: 0-2047)").pack()
tk.Label(master=frame9,text=f"Downstream Strength: {downstream_strength} (Range: 0-2047)").pack()
tk.Label(master=frame9,text=f"Ratio of travel time: {rate_travel_time} (Range: 0-2047)").pack()
tk.Label(master=frame9,text=f"Reynolds Number: {reynolds_number}").pack()

window.mainloop()

