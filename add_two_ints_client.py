#!/usr/bin/env python
# from tuts
import sys
import rospy
from agitr.srv import *

def add_two_ints_client(x, y):
	# No need to call init_node()
	rospy.wait_for_service('add_two_ints') # Blocks thread until add_two_ints 
	try:
		# rospy.ServiceProxy is a container for a request and response type. 
		# needs to be used whenever a service is called
		add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts) 
		respl = add_two_ints(x, y)
		return respl.sum
	except rospy.ServiceException, e:
		print "Service Call failed: %s" %e

def usage():
	return "%s [x y]" %sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s+%s"%(x, y)
    print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))


"""
(1) ... where we now request.
The request uses ServiceProxy as a wrapper for the request
then returns
"""