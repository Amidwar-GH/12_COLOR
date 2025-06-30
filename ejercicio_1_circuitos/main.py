#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

ev3 = EV3Brick()
motor_izq = Motor(Port.B)
motor_der = Motor(Port.C)
sensor_color = ColorSensor(Port.S3)

VELOCIDAD_AVANCE = 30
Entrada_deluz = 30

while True:
    reflejo = sensor_color.reflection()

    if reflejo < Entrada_deluz:
        if reflejo < Entrada_deluz - 10:  
            motor_izq.stop(Stop.BRAKE)
            motor_der.run(VELOCIDAD_AVANCE)
        else:
            motor_izq.run(VELOCIDAD_AVANCE)
            motor_der.run(VELOCIDAD_AVANCE)
    else:
        motor_izq.stop(Stop.BRAKE)
        motor_der.stop(Stop.BRAKE)

    wait(20) 



