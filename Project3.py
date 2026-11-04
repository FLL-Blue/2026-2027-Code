#await m.run_for_time(B, time2, -vel2)

from hub import port, motion_sensor
import time
import motor as m
import runloop as rl
A = port.A
B = port.B
D = port.D
E = port.E
F = port.F

AY = A
AV = B

R = F
L = E

async def code(vel1 = 360, vel2 = 180, time1 = 2000, time2 = 250, time3 = 550):
    await m.run_to_relative_position(B, 275, -180)
    m.run_for_time(F, time1, vel1)
    await m.run_for_time(E, time1, -vel1)
    m.run_for_time(F, time3, vel1)
    await m.run_for_time(E, time3, vel1)
    await m.run_to_relative_position(B, 275, 180)
    await m.run_for_time(A, time1, vel1)


rl.run(code())
