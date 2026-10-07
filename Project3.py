#mission 3 
"""
Needs to move forwards, rotate 45, forwards, 45deg and backwards. 45 degrees, full length.
Clockwise for all.
"""
import color
import color_sensor
import motor 
from hub import port

async def main():
    motor.run_for_degrees(port.A, 2160, 360)
    motor.run_for_degrees(port.B, 2160, 360)
