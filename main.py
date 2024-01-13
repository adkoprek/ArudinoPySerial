import serial
import tkinter as tk
import threading
import json
import enum

# Connect to the ARDUINO on Linux the device is mounted under /dev
# on windows it is as COM + number
ARDUINO = serial.Serial(port='/dev/ttyACM0', baudrate=9600)


# Create an Enum with the commands and the LEDS
class LEDS(enum.Enum):
    LED1 = 0


class Commands(enum.Enum):
    TOGGLE_LED_1 = '0'.encode()


# Create an abstract tkinter window
class MainWindow(tk.Tk):
    a0_text = None

    def __init__(self):
        super().__init__()
        self.set_up_window()
        self.set_up_receiver()
        self.geometry('200x200')
        self.mainloop()

    def set_up_window(self):
        # Create a String Variable for the label of A0
        self.a0_text = tk.StringVar()
        self.a0_text.set('loading...')

        # Create a Label to display the value of a0
        tk.Label(self, text='A0 Value').pack()
        tk.Label(self, textvariable=self.a0_text).pack()

        # Create a button to toggle the LED
        tk.Button(self, text='Toggle LED',
                  command=lambda: self.toggle_led(LEDS.LED1)).pack()

    def set_up_receiver(self):
        # Make a new thread tha twill receive and update the state of A0
        thread = threading.Thread(target=self.serial_callback, args=())
        thread.start()

    def serial_callback(self):
        while True:
            if ARDUINO.in_waiting > 0:
                # red the data and decode it
                data = ARDUINO.readline().decode('ascii')
                if data != '':
                    try:
                        # serialize the JSON message
                        serialized_data = json.loads(data)
                        self.a0_text.set(serialized_data['a0'])

                    except ValueError:
                        print('While parsing the message an error occurred')

    @staticmethod
    def toggle_led(led):
        # Check which LED has to be toggled
        if led == LEDS.LED1:
            ARDUINO.write(Commands.TOGGLE_LED_1.value)


if __name__ == '__main__':
    # Create an instance of the app
    _ = MainWindow()
