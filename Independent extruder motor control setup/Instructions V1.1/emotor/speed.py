from TMC_2209.TMC_2209_StepperDriver import *
import time
import sys



speed = int(sys.argv[1])

print("---")
print("SCRIPT START")
print("---")





#-----------------------------------------------------------------------
# initiate the TMC_2209 class
# use your pin for pin_en here
#-----------------------------------------------------------------------
tmc = TMC_2209(21)


tmc.set_loglevel(Loglevel.DEBUG)
tmc.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)



tmc.set_direction_reg(False)
tmc.set_current(370)
tmc.set_interpolation(True)
tmc.set_spreadcycle(False)
tmc.set_microstepping_resolution(256)
tmc.set_internal_rsense(False)


print("---\n---")


tmc.readIOIN()
tmc.readCHOPCONF()
tmc.readDRVSTATUS()
tmc.readGCONF()

print("---\n---")

#-----------------------------------------------------------------------
# activate the motor current output
#-----------------------------------------------------------------------
tmc.set_motor_enabled(True)

print("lefty speed is : ")
print(speed)


if speed == 0:
	tmc.set_deinitialize_false()
	tmc.set_motor_enabled(False)

	tmc.deinit()
	del tmc

else:
	tmc.set_vactual(speed)
	tmc.set_deinitialize_true()





print("---\n---")




print("---")
print("SCRIPT FINISHED")
print("---")
