#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()



motor_izq = Motor(Port.B)
motor_der = Motor(Port.C)
sensor_color = ColorSensor(Port.S3)


VELOCIDAD_BASE = 40

UMBRAL = 30

Ganancia = 1.2

while True:
    reflejo = sensor_color.reflection()  

    error = UMBRAL - reflejo  

    correccion = Ganancia * error

    velocidad_izq = VELOCIDAD_BASE + correccion
    velocidad_der = VELOCIDAD_BASE - correccion

    
    velocidad_izq = max(min(velocidad_izq, 100), 0)
    velocidad_der = max(min(velocidad_der, 100), 0)

    
    motor_izq.run(velocidad_izq)
    motor_der.run(velocidad_der)

    wait(10)





# Write your program here.
    
