import time
import board
import digitalio

# Set up the LED pin
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Blink the LED quickly
while True:
    led.value = True    # LED on
    time.sleep(0.05)    # Short delay
    led.value = False   # LED off
    time.sleep(0.05)    # Short delay
