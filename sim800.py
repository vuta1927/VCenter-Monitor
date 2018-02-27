import RPi.GPIO as GPIO
import serial
import time
import sys
import datetime

GPIO.setmode(GPIO.BOARD)
SERIAL_PORT = "/dev/ttyS0"
# Enable Serial Communication
ser = serial.Serial(SERIAL_PORT, baudrate=9600, timeout=5)
ser.read(ser.inWaiting())
while True:
    ser.write('AT'+'\r')
    rcv = ser.read(ser.inWaiting())
    print(str(rcv))
    time.sleep(3)
    if 'OK' in str(rcv):
        ser.write('AT+CMGF=1\r')
        rcv = ser.read(ser.inWaiting())
        time.sleep(3)
        print(str(rcv))
        if 'OK' in str(rcv):
            ser.write('AT+CMGS="01213270076"\r')
            rcv = ser.read(ser.inWaiting())
            time.sleep(3)
            print(str(rcv))
            if chr(62) in str(rcv):
                print('found!!!')
                ser.write('test'+chr(26))
                time.sleep(3)
                rcv = ser.read(ser.inWaiting())
                print(str(rcv))
    time.sleep(3)
    # ser.read(ser.inWaiting())
    # time.sleep(5)

