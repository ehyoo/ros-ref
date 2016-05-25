#!/usr/bin/env python
import rospy
#transposed

def throw():
	rospy.init_node('warn', anonymous = True)
	rate = rospy.Rate(10)
	for i in range(1,21):
		rospy.logdebug("counted to " + str(i))
		if i % 3 == 0:
			rospy.logwarn(str(i) + " is divisible by 3")
		if i % 5 == 0:
			rospy.loginfo(str(i) + " is divisible by 5")
		if i % 10 == 0:
			rospy.logerr(str(i) + " is divisible by 10")
		if i % 20 == 0:
			rospy.logfatal(str(i) + " is divisible by 20")
	rate.sleep()
# no python version of "ROS_DEBUG_STREAM_ONCE" or any variant
# if you really need it you can use a variable that stores a boolean value

if __name__ == "__main__":
	try:
		throw()
	except rospy.ROSInterruptException:
		pass
