#!/usr/bin/env python

import rospy

if __name__=='__main__':

	rospy.init_node('besheli')
	rospy.loginfo("Welcome to test world")

	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		rospy.loginfo("hello")
		rate.sleep()


