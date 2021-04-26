import serial


ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM7'
ser.open()
if ser.is_open:
    ser.write(b'AT+CMGF=1\r\n')
    ser.write(b'AT+CMGS="+79201111582"\r\n')
    ser.write(b'Testing 0001')
    ser.write(b'\x1A')
    ser.close()
