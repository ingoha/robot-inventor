from mindstorms import MSHub
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

async def run_animation(frames, clear=False, delay=500, loop=True, fade=4):
    while True:
        for f in frames:
            img = hub.Image(f)
            hub.display.show(img)
            sleep(delay/1000)
            yield
        if not loop:
            return
        
# Write your program here.
mshub.status_light.on('red')
hub.display.rotation(90)
anim=run_animation(animation_scanning)
while True:
    try:
        anim.send(None)
        # do something else...
    except StopIteration as e:
        print('animation finished')
        break
    
