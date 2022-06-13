## ---- Imports ---- ##
import board
from digitalio import Pull
from piper_blockly import *
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

## ---- Definitions ---- ##
LEFT_old = None
SPACE_old = None
RIGHT_old = None
DOWN_old = None
UP_old = None
UP = None
CLICK_old = None
LEFT = None
SPACE = None
RIGHT = None
DOWN = None
CLICK = None
GP11 = piperPin(board.GP11, "GP11")

try:
  set_digital_view(True)
except:
  pass

time.sleep(1)
keyboard_HID = Keyboard(usb_hid.devices)
keyboard_HID_layout = KeyboardLayoutUS(keyboard_HID)

GP14 = piperPin(board.GP14, "GP14")

# LINKE PFEILTASTE

def Key_LEFT_Service_Loop():
  global LEFT_old, SPACE_old, RIGHT_old, DOWN_old, UP_old, UP, CLICK_old, LEFT, SPACE, RIGHT, DOWN, CLICK
  LEFT_old = LEFT
  print(GP11.checkPin(None))
  if GP11.checkPin(None):
    LEFT = 1
  else:
    LEFT = 0
  time.sleep(0.01)
  if LEFT > LEFT_old:
    keyboard_HID.press(Keycode.LEFT_ARROW)
    GP14.setPin(1)
  elif LEFT < LEFT_old:
    keyboard_HID.release(Keycode.LEFT_ARROW)
    GP14.setPin(0)

GP1 = piperPin(board.GP0, "GP0")
GP1 = piperPin(board.GP1, "GP1")
GP2 = piperPin(board.GP2, "GP2")
GP26 = piperPin(board.GP26, "GP26")
GP27 = piperPin(board.GP27, "GP27")
GP28 = piperPin(board.GP28, "GP28")

# Describe this function...
def Key_SPACE_Service_Loop():
  global LEFT_old, SPACE_old, RIGHT_old, DOWN_old, UP_old, UP, CLICK_old, LEFT, SPACE, RIGHT, DOWN, CLICK
  SPACE_old = SPACE
  if GP21.checkPin(None):
    SPACE = 1
  else:
    SPACE = 0
  time.sleep(0.01)
  if SPACE > SPACE_old:
    keyboard_HID.press(Keycode.SPACEBAR)
    GP14.setPin(1)
  elif SPACE < SPACE_old:
    keyboard_HID.release(Keycode.SPACEBAR)
    GP14.setPin(0)

GP12 = piperPin(board.GP12, "GP12")
# Describe this function...
def Key_RIGHT_Service_Loop():
  global LEFT_old, SPACE_old, RIGHT_old, DOWN_old, UP_old, UP, CLICK_old, LEFT, SPACE, RIGHT, DOWN, CLICK
  RIGHT_old = RIGHT
  if GP12.checkPin(None):
    RIGHT = 1
  else:
    RIGHT = 0
  time.sleep(0.01)
  if RIGHT > RIGHT_old:
    keyboard_HID.press(Keycode.RIGHT_ARROW)
    GP14.setPin(1)
  elif RIGHT < RIGHT_old:
    keyboard_HID.release(Keycode.RIGHT_ARROW)
    GP14.setPin(0)

GP13 = piperPin(board.GP13, "GP13")
# Describe this function...
def Key_DOWN_Service_Loop():
  global LEFT_old, SPACE_old, RIGHT_old, DOWN_old, UP_old, UP, CLICK_old, LEFT, SPACE, RIGHT, DOWN, CLICK
  DOWN_old = DOWN
  if GP13.checkPin(None):
    DOWN = 1
  else:
    DOWN = 0
  time.sleep(0.01)
  if DOWN > DOWN_old:
    keyboard_HID.press(Keycode.DOWN_ARROW)
    GP14.setPin(1)
  elif DOWN < DOWN_old:
    keyboard_HID.release(Keycode.DOWN_ARROW)
    GP14.setPin(0)

GP10 = piperPin(board.GP10, "GP10")
# Describe this function...
def Key_UP_Service_Loop():
  global LEFT_old, SPACE_old, RIGHT_old, DOWN_old, UP_old, UP, CLICK_old, LEFT, SPACE, RIGHT, DOWN, CLICK
  UP_old = UP
  if GP10.checkPin(None):
    UP = 1
  else:
    UP = 0
  time.sleep(0.01)
  if UP > UP_old:
    keyboard_HID.press(Keycode.UP_ARROW)
    GP14.setPin(1)
  elif UP < UP_old:
    keyboard_HID.release(Keycode.UP_ARROW)
    GP14.setPin(0)

# Describe this function...
def all_Variables_to_0():
  global LEFT_old, SPACE_old, RIGHT_old, DOWN_old, UP_old, UP, CLICK_old, LEFT, SPACE, RIGHT, DOWN, CLICK
  UP = 0
  UP_old = 0
  CLICK = 0
  CLICK_old = 0
  DOWN = 0
  DOWN_old = 0
  LEFT = 0
  LEFT_old = 0
  RIGHT = 0
  RIGHT_old = 0
  SPACE = 0
  SPACE_old = 0

GP20 = piperPin(board.GP20, "GP20")
mouse_HID = Mouse(usb_hid.devices)

# Describe this function...
def Mouse_CLICK_Service_Loop():
  global LEFT_old, SPACE_old, RIGHT_old, DOWN_old, UP_old, UP, CLICK_old, LEFT, SPACE, RIGHT, DOWN, CLICK
  CLICK_old = CLICK
  if GP20.checkPin(None):
    CLICK = 1
  else:
    CLICK = 0
  time.sleep(0.01)
  if CLICK > CLICK_old:
    mouse_HID.press(Mouse.LEFT_BUTTON)
    GP14.setPin(1)
  elif CLICK < CLICK_old:
    mouse_HID.release(Mouse.LEFT_BUTTON)
    GP14.setPin(0)


## ---- Code ---- ##
all_Variables_to_0()
GP1.setPin(1)
GP2.setPin(1)
GP3.setPin(1)
GP4.setPin(1)
GP5.setPin(1)
GP6.setPin(1)
GP7.setPin(1)
while True:
  Key_UP_Service_Loop()
  Key_DOWN_Service_Loop()
  Key_LEFT_Service_Loop()
  Key_RIGHT_Service_Loop()
  Key_SPACE_Service_Loop()
  Mouse_CLICK_Service_Loop()

  time.sleep(0.01)
