#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()


color_sensor = ColorSensor(Port.S3)



while True:
    #ev3.screen.print('no AMARILLO')
    if color_sensor.color() == Color.YELLOW:
        #ev3.speaker.beep()
        ev3.screen.print('AMARILLO')
    elif color_sensor.color()== Color.RED :
        ev3.screen.print('ROJO')
    elif color_sensor.color() == Color.GREEN:
        ev3.screen.print('Verde')
    elif color_sensor.color() == Color.BLACK:
        ev3.screen.print('Negro')
    elif color_sensor.color() == Color.BLUE:
        ev3.screen.print('Azul')
    elif color_sensor.color() == Color.WHITE:
        ev3.screen.print('BLANCO')
    elif color_sensor.color() == Color.BROWN:
        ev3.screen.print('MARRON')
    else:
        ev3.screen.print('Ninguno')