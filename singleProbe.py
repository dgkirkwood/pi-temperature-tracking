import os
import time

tempSensors = ['28-041781e887ff', '28-041781b282ff', '28-041781a26eff', '28-0317714b31ff', '28-031771e93cff']

temp_output = ''

#temp_sensor = '/sys/bus/w1/devices/28-031771c6acff/w1_slave'

def temp_raw(temp_sensor):
	sensorAddress = '/sys/bus/w1/devices/'+temp_sensor+'/w1_slave'
	#print(sensorAddress)
	f = open(sensorAddress, 'r')
	lines = f.readlines()
	f.close
	#print(lines)	
	return lines

def read_temp(sensor):


	lines = temp_raw(sensor)
	#print(lines)
	if lines[0].strip()[-3:] == 'YES':
		#print("YARRRP")
		time.sleep(0.2)
		temp_output = lines[1].find('t=')
	if temp_output != -1:
		temp_string = lines[1].strip()[temp_output+2:]
		temp_c = float(temp_string) / 1000.0
		return temp_c

while True:
	for sensor in tempSensors:
		print(sensor)
		print(read_temp(sensor))
		time.sleep(1)
