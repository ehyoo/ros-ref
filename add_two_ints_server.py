#!/usr/bin/env python
# from tuts
from agitr.srv import *
import rospy

def handle_add_two_ints(req):
    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    # makes a new service named "add_two_ints" with AddTwoInts as a service type
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print "Ready to add two ints."
    rospy.spin() # waits for shutdown

if __name__ == "__main__":
    add_two_ints_server()


"""
How this works:
Server itself is a node.
Node creates a service named "add_two_ints"
	as you might remember, AddTwoInts is detailed in AddTwoInts.srv: requests and responses
So the server is ready and waits for a response from the client... (1)

"""