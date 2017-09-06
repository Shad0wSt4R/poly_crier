#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)

def listener():
	rospy.init_node('listener')
	sub = rospy.Subscriber('names', String, callback)
	rospy.spin()
if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass
