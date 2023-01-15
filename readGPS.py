import serial
import pynmea2

while True:
	port="/dev/ttyACM0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout = pynmea2.NMEAStreamReader()
	# converting bytes to string: https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
	newdata=ser.readline().decode("utf-8")
	if newdata[0:6] == '$GNRMC':
		newmsg=pynmea2.parse(newdata)
		lat=newmsg.latitude
		lng=newmsg.longitude
		gps =  " \"name\":\"map\", \"lat\":" + lat + ", \"lon\":" + lng +" "
		# gps = "Latitude=" + str(lat) + " Longitude=" + str(lng)
		print(gps)


