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

def calibrate():
		# run motor until it stalls (timeout 3s)
		start_time_ms = time.ticks_us()
		chest_motor.run_at_speed(-75)
		
		while True:
				# cf. https://github.com/maarten-pennings/Lego-Mindstorms/blob/main/ms4/faq.md#what-is-motorget
				speed = chest_motor.get()[0]

				_delta_t_ms = (time.ticks_us() - start_time_ms) / 1000
				if (_delta_t_ms > 3000):
						break
				elif (_delta_t_ms > 100 and speed == 0):
						print ('no more movement')
						break
		# stop motor
		chest_motor.pwm(0)
		# start counting delta yaw
		# run motor back until delta yaw=42
		
		return

# Write your program here.
mshub.status_light.on('red')
hub.display.rotation(90)
hub.sound.play('/extra_files/Scanning')
anim=[]
for frame in animation_scanning:
    img = hub.Image(frame)
    anim.append(img)

calibrate()

hub.display.show(anim, wait=False, loop=True)

sys.exit()