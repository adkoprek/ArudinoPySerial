# PSI
A basic example of a python GUI to read and write to a Aduino over the serial port. In this example a Arduino UNO was used and the functinoallity is based on reading the a0 analog input port and sending the data over serial in a JSON format. The Arduino UNO also has a command that can be send over the serial console to toggle the pin 13, you just have to send 0.

The project consists of 2 parts the Arduino Sketch `PSI.ino` and the python GUI `main.py`

## The needed Libraries are
  - Tkinter: `pip install tk`
  - Serial: `pip isntall pyserial`
  - The rest should be installed with your python installation 

## The needed Tools are
  - Python 3 interpreter
  - Arduino IDE
