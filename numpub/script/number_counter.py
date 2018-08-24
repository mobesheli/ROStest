#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

count = 0

def handle(req):
	if req.data:
		global count
		count = 0
		return True, 'reset'	
	return False, 'no reset'

def callback(msg):
	global count
	count = count + 1
	pub = rospy.Publisher('/number_count', Int64, queue_size=10)
	rate=rospy.Rate(10)
	print count			
	pub.publish(count)
	# rate.sleep()
	

def listenandtalk():

	rospy.init_node('number_counter', anonymous=True)
	sub=rospy.Subscriber("/number", Int64, callback)
	rospy.spin()
	

if __name__=='__main__':

	service = rospy.Service('/resetc', SetBool, handle)
	listenandtalk()
	rospy.loginfo("SRV created")
	rospy.spin()
	print count


