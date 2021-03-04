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

# cf. https://github.com/maarten-pennings/Lego-Mindstorms/blob/main/ms4/faq.md#what-is-motorget
class MotorAsync:
		def __init__(self, port):
				self.motor = Motor(port)
		
		def run_until_stall(self, direction = 1, pwm=100, timeout_ms=3000):
				_speed = direction * int(pwm / 1.27)
				self.motor.set_default_speed(_speed)
				start_time_ms = time.ticks_us()
				self.motor.start()
				start_degrees_counted = self.motor.get_degrees_counted()

				while True:
						_delta_t_ms = (time.ticks_us() - start_time_ms) / 1000
						if (_delta_t_ms > timeout_ms):
								break
						elif (_delta_t_ms > 100 and self.motor.get_speed() == 0):
								print ('no more movement')
								break
						else:
								yield
				
				self.motor.stop()
				return

		def run_for_degrees(self, degrees, speed=75):
				direction = 1
				if(degrees < 0):
						direction = -1
				
				# default speed is 75...
				_speed = direction * speed

				self.motor.set_degrees_counted(0)

				# start motor at speed +/-20
				self.motor.set_default_speed(_speed)
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

def calibrate():
		stall = chest_motor.run_until_stall()
		while True:
				try:
						stall.send(None)
						yield
				except StopIteration as e:
						break
		
		# TODO: run back until yaw=42

		return


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
hub.display.rotation(90)
hub.sound.play('/extra_files/Scanning')
anim=[run_animation(animation_scanning)]
move=[calibrate()]
threads=[anim,move]
# fill thread array
threads_stepcounter=[0,0]
active_threads = 2

while True:
	for i, t in enumerate(threads):
		step = threads_stepcounter[i]
		if step == -1:
			continue
		try:
			t[step].send(None)
		except StopIteration as e:
			print('thread finished')
			# another one in queue?
			if step < len(t) - 1:
				threads_stepcounter[i] += 1
			else:
				threads_stepcounter[i] = -1
				active_threads -= 1
				print('active threads: ', str(active_threads))
				if active_threads == 0:
					sys.exit()

