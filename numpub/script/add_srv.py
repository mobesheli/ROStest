#!/usr/bin/env python

import rospy
from rospy_tutorials.srv import AddTwoInts

def handle(req):
	result=req.a + req.b
	rospy.loginfo('Sum of '+ str(req.a) +' and '+ str(req.b)+ " is " + str(result))
	return result
if __name__=='__main__':
	rospy.init_node('add_srv')
	rospy.loginfo('Add two ints node created')
	service = rospy.Service('/add_two_ints', AddTwoInts, handle)
	rospy.loginfo("SRV created")
	rospy.spin()

