#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__=='__main__':
	rospy.init_node('rnews_transmitter')
	pub = rospy.Publisher('/robot_news', String, queue_size=10) 
	rate=rospy.Rate(2)
	while not rospy.is_shutdown():
		msg = String()
		msg.data="Hello people"
		pub.publish(msg)
		rate.sleep()
	rospy.loginfo("node stopped")

