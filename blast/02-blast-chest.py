from mindstorms import MSHub, Motor
import hub
import time
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

# cf. https://github.com/maarten-pennings/Lego-Mindstorms/blob/main/ms4/faq.md#what-is-motorget
class MotorAsync:
    def __init__(self, port):
        self.motor = Motor(port)
        
    def run_for_degrees(self, degrees):
        direction = 1
        if(degrees < 0):
            direction = -1
        
        # default speed is 75...
        speed = direction * 20

        self.motor.set_degrees_counted(0)

        # start motor at speed +/-20
        self.motor.set_default_speed(speed)
        self.motor.start()
        while True:
            if(direction * ((self.motor.get_degrees_counted()) - degrees) < 0):
                yield self.motor.get_degrees_counted()
            else:
                break
        # stop motor
        self.motor.stop()
        return

chest_motor = MotorAsync('D')

def run_animation(frames, clear=False, delay_ms=500, loop=True, fade=4):
    while True:
        for f in frames:
            start_time_ms = time.ticks_us()
            img = hub.Image(f)
            hub.display.show(img)
            while((time.ticks_us() - start_time_ms) / 1000 < delay_ms):
                #print((time.ticks_us() - start_time_us) * 1000)
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
hub.display.clear()
hub.display.rotation(90)
anim=run_animation(animation_scanning)
#move=run_move()
move=chest_motor.run_for_degrees(500)
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
        # FIXME stops animation as well...
        break
    
