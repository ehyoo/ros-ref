#!/usr/bin/env python
#transposed
import rospy
from geometry_msgs.msg import Twist
import random as rand

def turtle_controller():
	# Publisher object
	pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 1000)
	# init ros system and become a node
	rospy.init_node('turtle_controller', anonymous = True)
	# loop at 2Hz
	rate = rospy.Rate(2)
	while not rospy.is_shutdown():
		msg = Twist()
		msg.linear.x = rand.random()
		msg.angular.z = rand.random() 
		pub.publish(msg)
		rate.sleep()


if __name__ == '__main__':
	try:
		turtle_controller()
	except rospy.ROSInterruptException:
		pass

# dude it worked
