# Tinkertank's Frisbee - the sustainable Microcontroller

The Frisbee is your perfect tool to make new inventions out of e-waste, old toys and everyday objects.

![front](https://user-images.githubusercontent.com/84087178/173510615-f74fed8c-3dc6-49c0-a81b-748b4ae2a8a8.png)

The Frisbee is a microcontroller that can be plugged into any computer via USB and is recognized as a keyboard. Thus, similar to the Makey Makey ( https://makeymakey.com/ ), all conductive objects can be used to close circuits and trigger keystrokes. So a fork stuck in an apple becomes a space bar, or a high-five with your best friend becomes an arrow key.
If you still haven't had enough, you can turn the frisbee upside down to the dark side and dive deeper into the rabbit hole of makers and coders. On the backside and with the help of a block-based programming platform like OpenRoberta it is easy to run every actuator and sensor you find in the electronic waste to make your idea reality.

![darkside](https://user-images.githubusercontent.com/84087178/173510602-0f383d07-d8e2-4701-b765-c77271a8d3dc.png)
<br>*dark side of the ~~moon~~ frisbee*

# another microcontroller?

yes, why not.
it's plug and play like a [Makey Makey](https://makeymakey.com/), it's easy to reprogram like the [Micro:bit](https://microbit.org//), it's cheap like an [Arduino Nano](https://store.arduino.cc/collections/most-popular/products/arduino-nano-every-with-headers) and it's capable of running micropython for super fast and compile-free programming.
Aaaaand it's got a super sweet RG-Bee-LED shining through the pcb for instant feedback. (reverse mounted neopixel LED)

# comparison sheet
|                            | Arduino Uno          | Makey Makey            | Micro:Bit            | Calliope          | Frisbee 2.0              |
| -------------------------- | -------------------- | ---------------------- | -------------------- | ----------------- | ------------------------ |
| Image                      |                      |                        |                      |                   |                          |
| forked from                |                      | Pro Micro /<br>Arduino Leonardo |             | Micro:Bit         | Raspberry Pi Pico        |
|                            |                      |                        |                      |                   |                          |
| hardware connectors        | jumper wires         | alligator clips   | alligator clips (limited) | alligator clips   | alligator clips          |
| cpu | ATmega328 (8-bit) | Atmel 32U4 | ARM Cortex-M0 (Nordic nRF51822) mit 32-Bit | ARM Cortex-M0 (Nordic nRF51822) mit 32-Bit | dual-core Arm Cortex-M0+ |
| native node based programming | NO                | NO                     | YES                  | YES               | YES                      |
| Bluetooth                  | NO                   | NO                     | YES                  | YES               | NO                       |
| Wifi                       | NO                   | NO                     | NO                   | NO                | NO                       |
| additional periphery       | LED                  | LED                    | Lagesensor, Buttons, LED Matrix, Kompass, RGB-LED, Temperatur, Lautsprecher, Mikrofon   | Lagesensor, Buttons, LED Matrix, Kompass, RGB-LED, Temperatur, Lautsprecher, Mikrofon | LED   |
| plug and play input device | NO                   | YES                    | NO                   | NO                | YES                      |
| made in                    | china                | china                  | ?                    | ?                 | D                        |
| hareware cost              | 23,50 €              | 55,00 €                | 29,00 €              | 40,00 €           | 15,00 €                  |

# fair trade & regional
We try to produce the frisbee boards as sustainable as possible and under fair working conditions in germany.
We are experimenting with different technologies like Paper-PCBs or printing with conductive paint on wood as an eco-friendly alternative to epoxy-based PCBs.

# open source
The Frisbee, like its core, the Pi Pico, is completely open source and can be further developed, modified and used by all users under the Creative Commons 4.0 license.

# about
Tinkertank is a stationary and mobile makerspace based in Ludwigsburg, Germany, empowering kids and adults to the creative use of technology.
www.tinkertank.de
