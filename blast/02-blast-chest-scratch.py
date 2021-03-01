from util.print_override import spikeprint;print = spikeprint
import hub
from runtime import VirtualMachine
from util.rotation import rotate_hub_display_to_value
from util.scratch import convert_animation_frame, number_color_to_rgb, pitch_to_freq

g_animation = ["0000000000567890000000000", "0000000000456980000000000", "0000000000349870000000000", "0000000000298760000000000", "0000000000987650000000000", "0000000000896540000000000", "0000000000789430000000000", "0000000000678920000000000"]

async def stack_1(vm, stack):
    hub.led(*number_color_to_rgb(9))
    rotate_hub_display_to_value("2")
    global g_animation
    brightness = vm.store.display_brightness()
    frames = [hub.Image(convert_animation_frame(frame, brightness)) for frame in g_animation]
    vm.system.display.show(frames, clear=False, delay=200, loop=True, fade=2)
    vm.system.sound.play("/extra_files/Scanning", freq=pitch_to_freq(vm.store.sound_pitch(), 12000, 16000, 20000))
    (acceleration, deceleration) = vm.store.motor_acceleration("D")
    vm.store.motor_last_status("D", await vm.system.motors.on_port("D").run_for_degrees_async(500, vm.store.motor_speed("D"), stall=vm.store.motor_stall("D"), stop=vm.store.motor_stop("D"), acceleration=acceleration, deceleration=deceleration))
    (acceleration_1, deceleration_1) = vm.store.motor_acceleration("D")
    vm.store.motor_last_status("D", await vm.system.motors.on_port("D").run_for_degrees_async(1000, -vm.store.motor_speed("D"), stall=vm.store.motor_stall("D"), stop=vm.store.motor_stop("D"), acceleration=acceleration_1, deceleration=deceleration_1))
    (acceleration_2, deceleration_2) = vm.store.motor_acceleration("D")
    vm.store.motor_last_status("D", await vm.system.motors.on_port("D").run_for_degrees_async(500, vm.store.motor_speed("D"), stall=vm.store.motor_stall("D"), stop=vm.store.motor_stop("D"), acceleration=acceleration_2, deceleration=deceleration_2))

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "0TwE8utPyEt2wPSqDawo")

    vm.register_on_start("h8EqnFZU5g4RaOBhKDaI", stack_1)

    return vm
