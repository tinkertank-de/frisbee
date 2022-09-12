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

## ---- Definitions ---- ##

pinValueOld = [0,0,0,0,0,0] # previous pinValues
pinValue = [0,0,0,0,0,0]    # sum of pinValue Readings 
numReadings = 10			# number of readings before evaluating
threshold = 8    			# threshold to trigger key

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 20, 255)
BLACK = (0,0,0)
pxColor = BLACK

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

pixels = neopixel.NeoPixel(board.GP14, 1, brightness=1, auto_write=False)



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

## startup animation
def startup(pc):
    for k in range(80):
        pixels[0] = (k,k*pc,0)
        time.sleep(0.01)
        pixels.show()
        
    pixels[0] = (10,10*pc,0)
    pixels.show()
    time.sleep(0.1)
    pixels[0] = (80,80*pc,0)
    pixels.show()
    time.sleep(0.1)
    pixels[0] = (20,20*pc,0)
    pixels.show()
    time.sleep(0.1)
    pixels[0] = (255,255*pc,0)
    pixels.show()
    time.sleep(1)
    for k in range(0, 255):
        pixels[0] = (255-k,(255-k)*pc,0)
        time.sleep(0.001)
        pixels.show()

try:
    keyboard_HID = Keyboard(usb_hid.devices)
    mouse_HID = Mouse(usb_hid.devices)
except:
    startup(0) #startup animation in yellow
else:
    startup(1) #startup animation in red



## functions ##

def sensePin(pin):    # digital Read pins and add to 'pinValue' variable
    global pinValue  
    if pin == 0:                      
        pinValue[0] += Pin10.value
    elif pin == 1:
        pinValue[1] += Pin11.value
    elif pin == 2:
        pinValue[2] += Pin12.value
    elif pin == 3:
        pinValue[3] += Pin13.value
    elif pin == 4:
        pinValue[4] += Pin20.value
    elif pin == 5:
        pinValue[5] += Pin21.value

def evaluatePins():             # evaluate 'pinValue'
    for i in range(6):
        global pinValue, pinValueOld, pxColor 
        
        # print (pinValue[i], end=" ")    	# print raw sum values for debugging
        if pinValue[i] > threshold:			# see if pinValue is higher than threshold
            pinValue[i] = 1
            if i < 4: pxColor = GREEN		#arrow keys: green
            elif i == 4: pxColor = RED
            elif i == 5: pxColor = BLUE
            
        else:
            pinValue[i] = 0 # not pressed
            
        if pinValueOld[i] < pinValue[i]:
            try:
                if i == 0: keyboard_HID.press(Keycode.UP_ARROW)
                elif i == 1: keyboard_HID.press(Keycode.LEFT_ARROW)
                elif i == 2: keyboard_HID.press(Keycode.RIGHT_ARROW)
                elif i == 3: keyboard_HID.press(Keycode.DOWN_ARROW)
                elif i == 4: mouse_HID.press(Mouse.LEFT_BUTTON)
                elif i == 5: keyboard_HID.press(Keycode.SPACEBAR)
            except:
                p = 0
            else:
                p = 0
        elif pinValueOld[i] > pinValue[i]:
            try:
                if i == 0: keyboard_HID.release(Keycode.UP_ARROW)
                elif i == 1: keyboard_HID.release(Keycode.LEFT_ARROW)
                elif i == 2: keyboard_HID.release(Keycode.RIGHT_ARROW)
                elif i == 3: keyboard_HID.release(Keycode.DOWN_ARROW)
                elif i == 4: mouse_HID.release(Mouse.LEFT_BUTTON)
                elif i == 5: keyboard_HID.release(Keycode.SPACEBAR)
            except:
                p = 0
            else:
                p = 0
        pinValueOld[i] = pinValue[i]		# save previous value
        pinValue[i] = 0   					# reset RawValue
    
def readTouchPoint():
    global touch, pxColor
    if touch.value:
        pxColor =(YELLOW)



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



