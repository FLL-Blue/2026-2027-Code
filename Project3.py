from hub import port, motion_sensor
import time
import motor as m
import runloop as rl
 

async def forward(amount):
    m.run_for_degrees(R_WHEEL, amount, 360)
    await m.run_for_degrees(L_WHEEL, amount, -360)

async def arm_horizontal(amount, velocity):
    await m.run_for_degrees(ARM_HORIZONTAL, amount, velocity)

async def arm_verticle(amount, velocity):
    await m.run_zfor_degrees(ARM_VERTICLE, amount, velocity)

async def arm_simul(amount1, amount2, vel1, vel2):
    m.run_for_degrees(ARM_VERTICLE, amount1, vel1)
    await m.run_for_degrees(ARM_HORIZONTAL, amount2, vel2)

async def right(right):
    m.run_for_degrees(R_WHEEL, right, 720)
    await m.run_for_degrees(L_WHEEL, right, 360)

async def left(left):
    m.run_for_degrees(L_WHEEL, left, 360)
    await m.run_for_degrees(L_WHEEL, left, 720)


async def backwards(amount):
    m.run_for_degrees(R_WHEEL, amount, -360)
    await m.run_for_degrees(L_WHEEL, amount, 360) 



# async def code(vel1 = 360, vel2 = 180, time1 = 2000, time2 = 250, time3 = 550):
    # await m.run_for_degrees(B, 15, -25)
    # m.run_for_time(F, time1, vel1)
    # await m.run_for_time(E, time1, -vel1)
    # m.run_for_time(F, time3, vel1)
    # await m.run_for_time(E, time3, vel1)
    # await m.run_to_relative_position(A, 225, 240)
    # await m.run_for_time(A, time1, vel1)


rl.run(forward(900))
rl.run(left(360))
rl.run(forward(230))
rl.run(arm_verticle(20, -30))
rl.run(arm_simul(30, 120, 360, 200))
