#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_recieve(msg):
	rospy.loginfo("Message recieved: ")
	rospy.loginfo(msg)

if __name__=='__main__':
	rospy.init_node('smartphone')
	sup = rospy.Subscriber("/robot_news", String, callback_recieve)
	rospy.spin()
 
