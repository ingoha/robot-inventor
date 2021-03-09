from mindstorms import MSHub, Motor
from util.sensors import get_sensor_value, is_type
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
				# check timeout
				if (_delta_t_ms > 3000):
						break
				# 300ms after motor start, check if speed has dropped (=end position)
				elif (_delta_t_ms > 300 and speed >= -50):
						break
		# stop motor
		chest_motor.pwm(0)
		# start counting delta yaw
		start_yaw = hub.motion.position()[0]
		start_time_ms = time.ticks_us()
		# run motor back until delta yaw=42 (timeout 2000)
		chest_motor.run_at_speed(37)
		while True:
				_delta_t_ms = (time.ticks_us() - start_time_ms) / 1000
				_delta_yaw = abs((hub.motion.position()[0] - start_yaw))
				if (_delta_t_ms > 2000):
						break
				elif (_delta_yaw >= 42):
						break
		chest_motor.pwm(0)
		return

# Write your program here.
mshub.status_light.on('red')
hub.display.rotation(90)
hub.sound.play('/extra_files/Scanning')
anim=[]
for frame in animation_scanning:
    img = hub.Image(frame)
    anim.append(img)

hub.display.show(anim, wait=False, clear=False, delay=200, loop=True, fade=2)
calibrate()
chest_motor.run_for_degrees(648,speed=75)
# init sensor
port_f = getattr(hub.port, "F", None)
if getattr(port_f, "device", None) and is_type("F", 62):
		# turn on lights
		port_f.device.mode(5, b''+chr(9)+chr(9)+chr(9)+chr(9))

sys.exit()