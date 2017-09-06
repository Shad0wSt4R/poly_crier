#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from random import randint

def talker():
	# List of names to be printed
	words = ["Dr. Bushey", "Vamsi", "Jon"]
	
	# Registers with roscore a node called "talker". 
	# ROS programs are called nodes.
	rospy.init_node('talker')

	# Publisher object gets registered to roscore and creates a topic.
	pub = rospy.Publisher('names', String)
	
	# How fast names will be posted. In Hertz.
	rate = rospy.Rate(21)

	while not rospy.is_shutdown():
		number = randint(0,2)
		pub.publish(words[number])
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
