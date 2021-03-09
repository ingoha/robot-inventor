from mindstorms import MSHub, Motor
import hub
import time
import sys

# Create your objects here.
mshub = MSHub()

# g_animation = ["0000000000567890000000000",
#  "0000000000456980000000000", 
# "0000000000349870000000000", 
# "0000000000298760000000000",
#  "0000000000987650000000000", 
# "0000000000896540000000000", 
# "0000000000789430000000000", 
# "0000000000678920000000000"]

animation_scanning = ['00000:00000:56789:00000:00000', 
												'00000:00000:45698:00000:00000',
												'00000:00000:34987:00000:00000',
												'00000:00000:29876:00000:00000',
												'00000:00000:98765:00000:00000',
												'00000:00000:89654:00000:00000',
												'00000:00000:78943:00000:00000',
												'00000:00000:67892:00000:00000']

chest_motor = motor=hub.port.D.motor

# Write your program here.
mshub.status_light.on('red')
hub.display.rotation(90)
hub.sound.play('/extra_files/Scanning')
anim=[]
for frame in animation_scanning:
    img = hub.Image(frame)
    anim.append(img)

hub.display.show(anim, wait=False, loop=True)
#anim=[run_animation(animation_scanning)]
chest_motor.run_for_degrees(500,speed=100)
while chest_motor.busy(1):
		pass
chest_motor.run_for_degrees(1000,speed=-100)
while chest_motor.busy(1):
		pass
chest_motor.run_for_degrees(500,speed=100)
while chest_motor.busy(1):
		pass

sys.exit()