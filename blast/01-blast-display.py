from mindstorms import MSHub
import hub
import time

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
        
# Write your program here.
mshub.status_light.on('red')
hub.display.clear()
hub.display.rotation(90)
#anim=run_animation(animation_scanning)
anim=[]
for frame in animation_scanning:
    img = hub.Image(frame)
    anim.append(img)

hub.display.show(anim)
#while True:
#    try:
#        anim.send(None)
#        # do something else...
#        #print('yield')
#    except StopIteration as e:
#        print('animation finished')
#        break
    
