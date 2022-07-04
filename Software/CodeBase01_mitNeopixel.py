## ---- TINKERTANK FRISBEE ---- ##
## ------ standard code ------- ##

## ---- Imports ---- ##
import time
import board
import digitalio
import touchio
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
keyboard_HID = Keyboard(usb_hid.devices)
mouse_HID = Mouse(usb_hid.devices)

## ---- Definitions ---- ##

keyValue = [0,0,0,0,0,0] # current pinValue
keyValueOld = [0,0,0,0,0,0] # previous pinValue
keyValueRaw = [0,0,0,0,0,0] # sum of pinValue Readings 
readings = 0
numReadings = 10
threshold = 8

pixels = neopixel.NeoPixel(board.GP14, 1, brightness=1, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 20, 255)
PURPLE = (180, 0, 255)
BLACK = (0,0,0)
pxColor=BLACK

Pin10= digitalio.DigitalInOut(board.GP10)
Pin10.direction=digitalio.Direction.INPUT

Pin11= digitalio.DigitalInOut(board.GP11)
Pin11.direction=digitalio.Direction.INPUT

Pin12= digitalio.DigitalInOut(board.GP12)
Pin12.direction=digitalio.Direction.INPUT

Pin13= digitalio.DigitalInOut(board.GP13)
Pin13.direction=digitalio.Direction.INPUT

Pin20= digitalio.DigitalInOut(board.GP20)
Pin20.direction=digitalio.Direction.INPUT

Pin21= digitalio.DigitalInOut(board.GP21)
Pin21.direction=digitalio.Direction.INPUT

#touch
touch_pad = board.GP16
touch = touchio.TouchIn(touch_pad)

# all GPIOs to output high #

highPin0= digitalio.DigitalInOut(board.GP0)
highPin0.direction=digitalio.Direction.OUTPUT
highPin0.value = 1

highPin1= digitalio.DigitalInOut(board.GP1)
highPin1.direction=digitalio.Direction.OUTPUT
highPin1.value = 1

highPin2= digitalio.DigitalInOut(board.GP2)
highPin2.direction=digitalio.Direction.OUTPUT
highPin2.value = 1

highPin3= digitalio.DigitalInOut(board.GP26)
highPin3.direction=digitalio.Direction.OUTPUT
highPin3.value = 1

highPin4= digitalio.DigitalInOut(board.GP27)
highPin4.direction=digitalio.Direction.OUTPUT
highPin4.value = 1

highPin5= digitalio.DigitalInOut(board.GP28)
highPin5.direction=digitalio.Direction.OUTPUT
highPin5.value = 1


## functions ##

def sensePin(pinNr):
    global keyValueRaw
    
    ## pin Auslesen und zu 'keyValueRaw' hinzufügen
    if pinNr == 0:                      
        keyValueRaw[0] += Pin10.value
    elif pinNr == 1:
        keyValueRaw[1] += Pin11.value
    elif pinNr == 2:
        keyValueRaw[2] += Pin12.value
    elif pinNr == 3:
        keyValueRaw[3] += Pin13.value
    elif pinNr == 4:
        keyValueRaw[4] += Pin20.value
    elif pinNr == 5:
        keyValueRaw[5] += Pin21.value

def evaluatePins():
	for i in range(6):
		global keyValueRaw, keyValueOld, pxColor 
		
		# print (keyValueRaw[i], end=" ")    ## print raw sum values for debugging
		if keyValueRaw[i] > threshold:
			keyValueRaw[i] = 1
			if i < 4: pxColor = GREEN
			elif i == 4: pxColor = RED
			elif i == 5: pxColor = BLUE
			
		else:
			keyValueRaw[i] = 0
			
		if keyValueOld[i] < keyValueRaw[i]:
			if i == 0: keyboard_HID.press(Keycode.UP_ARROW)
			elif i == 1: keyboard_HID.press(Keycode.LEFT_ARROW)
			elif i == 2: keyboard_HID.press(Keycode.RIGHT_ARROW)
			elif i == 3: keyboard_HID.press(Keycode.DOWN_ARROW)
			elif i == 4: mouse_HID.press(Mouse.LEFT_BUTTON)
			elif i == 5: keyboard_HID.press(Keycode.SPACEBAR)
			
		elif keyValueOld[i] > keyValueRaw[i]:
			if i == 0: keyboard_HID.release(Keycode.UP_ARROW)
			elif i == 1: keyboard_HID.release(Keycode.LEFT_ARROW)
			elif i == 2: keyboard_HID.release(Keycode.RIGHT_ARROW)
			elif i == 3: keyboard_HID.release(Keycode.DOWN_ARROW)
			elif i == 4: mouse_HID.release(Mouse.LEFT_BUTTON)
			elif i == 5: keyboard_HID.release(Keycode.SPACEBAR)

		keyValueOld[i] = keyValueRaw[i]		# save previous value
		keyValueRaw[i] = 0   				# reset RawValue
	
def readTouchPoint():
    global touch, pxColor
    if touch.value:
        print ("touched")
        pxColor =(YELLOW)

## startup animation

for k in range(80):
    pixels[0] = (k,k,0)
    time.sleep(0.01)
    pixels.show()
	
pixels[0] = (10,10,0)
pixels.show()
time.sleep(0.1)
pixels[0] = (80,80,0)
pixels.show()
time.sleep(0.1)
pixels[0] = (20,20,0)
pixels.show()
time.sleep(0.1)
pixels[0] = YELLOW
pixels.show()
time.sleep(1)
for k in range(0, 255):
    pixels[0] = (255-k,255-k,0)
    time.sleep(0.001)
    pixels.show()

## ---- Code ---- ##
while True:
    pxColor = BLACK
    
    for i in range(numReadings):	#read [10] times
		for j in range(6):	
			sensePin(j)		# read all 6 Pins
		time.sleep(0.002)

    evaluatePins()
    readTouchPoint()

    pixels[0] = pxColor
    pixels.show()
    
    # print('')   #for debugging
