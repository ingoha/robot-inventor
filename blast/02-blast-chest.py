from mindstorms import MSHub, Motor
import hub
from time import sleep

# Create your objects here.
mshub = MSHub()

animation_scanning = ['00000:00000:56789:00000:00000', 
                        '00000:00000:34598:00000:00000',
                        '00000:00000:23987:00000:00000',
                        '00000:00000:19876:00000:00000',
                        '00000:00000:98765:00000:00000',
                        '00000:00000:89543:00000:00000',
                        '00000:00000:78932:00000:00000',
                        '00000:00000:67891:00000:00000']

chest_motor = Motor('D')

async def run_animation(frames, clear=False, delay=500, loop=True, fade=4):
    while True:
        for f in frames:
            img = hub.Image(f)
            hub.display.show(img)
            sleep(delay/1000)
            yield
        if not loop:
            return
        
async def run_move():
    # FIXME make motor movement async...
    chest_motor.run_for_degrees(500)
    yield
    chest_motor.run_for_degrees(-1000)
    yield
    chest_motor.run_for_degrees(500)
    return

# Write your program here.
mshub.status_light.on('red')
hub.display.rotation(90)
anim=run_animation(animation_scanning)
move=run_move()
while True:
    try:
        anim.send(None)
        # do something else...
    except StopIteration as e:
        print('animation finished')
        break
    try:
        move.send(None)
    except StopIteration as e:
        print('move finished')
        break
    
