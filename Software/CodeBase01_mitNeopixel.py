## ---- Imports ---- ##
import time
import board
import digitalio

import touchio

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

import neopixel



keyboard_HID = Keyboard(usb_hid.devices)
mouse_HID = Mouse(usb_hid.devices)

## ---- Definitions ---- ##
left_old = 0
right_old = 0
up_old = 0
click = 0
readings = 0
click_old = 0
space_old = 0
down_old = 0
left = 0
right = 0
up = 0
space = 0
down = 0

smoothed10=0;
smoothed11=0;
smoothed12=0;
smoothed13=0;
smoothed20=0;
smoothed21=0;

myReadings10=[0,0,0,0,0,0,0,0,0,0]
myReadings11=[0,0,0,0,0,0,0,0,0,0]
myReadings12=[0,0,0,0,0,0,0,0,0,0]
myReadings13=[0,0,0,0,0,0,0,0,0,0]
myReadings20=[0,0,0,0,0,0,0,0,0,0]
myReadings21=[0,0,0,0,0,0,0,0,0,0]



allCount=0
ledStatus = 0
readings=10


pixel_pin = board.GP14
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLACK = (0,0,0)
nextColor=BLACK

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



# funktions
def readPin10():
    global readings, up_old, up, allCount, smoothed10, myReadings10, ledStatus, nextColor
    if allCount == 0:
        up_old = up
        smoothed10= 0
        myReadings10=[0,0,0,0,0,0,0,0,0,0]
        
    if Pin10.value:
        myReadings10[smoothed10]=1
        smoothed10+=1                                                                                                                   
        


    if allCount == readings-1:
        print(myReadings10, end="")
        print(' : ', end="")
        
        if smoothed10 > 8:
            up = 1
            ledStatus = 1
            nextColor=GREEN
            print('high ', end="")
        else:
            up = 0
            print('low  ', end="")
        if up_old < up:
            keyboard_HID.press(Keycode.UP_ARROW)
        elif up_old > up:
            keyboard_HID.release(Keycode.UP_ARROW)


def readPin11():
    global readings, left_old, left, allCount, smoothed11, myReadings11, ledStatus, nextColor
    if allCount == 0:
        left_old = left
        smoothed11= 0
        myReadings11=[0,0,0,0,0,0,0,0,0,0]
        
    if Pin11.value:
        myReadings11[smoothed11]=1
        smoothed11+=1                                                                                                                   
        

    if allCount == readings-1:
        print(myReadings11, end="")
        print(' : ', end="")
        
        if smoothed11 > 8:
            left = 1
            ledStatus = 1
            nextColor=GREEN
            print('high ', end="")
        else:
            left = 0
            print('low  ', end="")
        if left_old < left:
            keyboard_HID.press(Keycode.LEFT_ARROW)
        elif left_old > left:
            keyboard_HID.release(Keycode.LEFT_ARROW)


def readPin12():
    global readings, right_old, right, allCount, smoothed12, myReadings12, ledStatus, nextColor
    if allCount == 0:
        right_old = right
        smoothed12= 0
        myReadings12=[0,0,0,0,0,0,0,0,0,0]
        
    if Pin12.value:
        myReadings12[smoothed12]=1
        smoothed12+=1                                                                                                                   
        

    if allCount == readings-1:
        print(myReadings12, end="")
        print(' : ', end="")
        
        if smoothed12 > 8:
            right = 1
            ledStatus = 1
            nextColor=GREEN
            print('high ', end="")
        else:
            right = 0
            print('low  ', end="")
        if right_old < right:
                keyboard_HID.press(Keycode.RIGHT_ARROW)
        elif right_old > right:
                keyboard_HID.release(Keycode.RIGHT_ARROW)


def readPin13():
    global readings, down_old, down, allCount, smoothed13, myReadings13, ledStatus, nextColor
    if allCount == 0:
        down_old = down
        smoothed13= 0
        myReadings13=[0,0,0,0,0,0,0,0,0,0]
        
    if Pin13.value:
        myReadings13[smoothed13]=1
        smoothed13+=1                                                                                                                   
        

    if allCount == readings-1:
        print(myReadings13, end="")
        print(' : ', end="")
        
        if smoothed13 > 8:
            down = 1
            ledStatus = 1
            nextColor=GREEN
            print('high ', end="")
        else:
            down = 0
            print('low  ', end="")
        if down_old < down:
            keyboard_HID.press(Keycode.DOWN_ARROW)
        elif down_old > down:
            keyboard_HID.release(Keycode.DOWN_ARROW)


def readPin20():
    global readings, click_old, click, allCount, smoothed20, myReadings20, ledStatus, nextColor
    if allCount == 0:
        click_old = click
        smoothed20= 0
        myReadings20=[0,0,0,0,0,0,0,0,0,0]
        
    if Pin20.value:
        myReadings20[smoothed20]=1
        smoothed20+=1                                                                                                                   
        

    if allCount == readings-1:
        print(myReadings20, end="")
        print(' : ', end="")
        
        if smoothed20 > 8:
            click = 1
            ledStatus = 1
            nextColor=RED
            print('high ', end="")
        else:
            click = 0
            print('low  ', end="")
        if click_old < click:
            mouse_HID.press(Mouse.LEFT_BUTTON)
        elif click_old > click:
            mouse_HID.release(Mouse.LEFT_BUTTON)
    
def readPin21():
    global readings, space_old, space, allCount, smoothed21, myReadings21, ledStatus, nextColor
    if allCount == 0:
        space_old = space
        smoothed21= 0
        myReadings21=[0,0,0,0,0,0,0,0,0,0]
        
    if Pin21.value:
        myReadings21[smoothed21]=1
        smoothed21+=1                                                                                                                   
        

    if allCount == readings-1:
        print(myReadings21, end="")
        print(' : ', end="")
        
        if smoothed21 > 8:
            space = 1
            ledStatus = 1
            nextColor=BLUE                                                                        
            print('high ', end="")
        else:
            space = 0
            print('low  ', end="")
        if space_old < space:
            keyboard_HID.press(Keycode.SPACEBAR)
        elif space_old > space:
            keyboard_HID.release(Keycode.SPACEBAR)

def readTouchPoint():
    global touch, nextColor, ledStatus
    if touch.value:
        print ("touched")
        nextColor =(YELLOW)
        ledStatus=1
    #time.sleep(0.05)

# startup animation

for k in range(0, 80):
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

pixels[0] = (255,255,0)
pixels.show()
time.sleep(0.1)

time.sleep(1)
for k in range(0, 255):
    pixels[0] = (255-k,255-k,0)
    time.sleep(0.001)
    pixels.show()
   
pixels[0] = (0,0,0)
pixels.show()


## ---- Code ---- ##
while True:
    
    ledStatus = 0
    

    for allCount in range(int(readings)):
        readPin10()
        readPin11()
        readPin12()
        readPin13()
        readPin20()
        readPin21()
        time.sleep(0.002);

    readTouchPoint()
        
    if ledStatus == 1:
        pixels[0]=(nextColor)
        pixels.show()
    else:
        pixels[0]=(BLACK)
        pixels.show()
        
    print('')
        
