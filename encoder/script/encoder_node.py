#!/usr/bin/python
# Put the description of your file here
# Author: Theo Long <lziaho1@vt.edu>

# Import the Default ROS tools
import rospy
from sensor_msgs.msg import Range
from sensor_msgs.msg import JointState
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import math
from quadrature import QuadratureEstimator
ADC.setup()
encoderRight = QuadratureEstimator()
encoderLeft = QuadratureEstimator()
left1="P8_7"
left2="P8_8"
right1="P8_9"
right2="P8_10"
GPIO.setup("P8_7", GPIO.IN)
GPIO.setup("P8_8", GPIO.IN)
GPIO.setup("P8_9", GPIO.IN)
GPIO.setup("P8_10", GPIO.IN)
if __name__ == '__main__':
  try:
  	rospy.init_node('encoder')
  	left=JointState()
  	right=JointState()
  	encoderRight.update(GPIO.input("P8_7"),GPIO.input("P8_8"),rospy.get_rostime().to_sec)
	left.position.append(encoderRight.position) 
	left.velocity.append(encoderRight.velocity)
	encoderLeft.update(GPIO.input("P8_9"),GPIO.input("P8_10"),rospy.get_rostime().to_sec)
	left.position.append(encoderLeft.position) 
	left.velocity.append(encoderLeft.velocity)
	pubRight = rospy.Publisher('/py_controller/rear_right_wheel/encoder', JointState, queue_size=10)
	pubRight.publish(right)
	pubLeft = rospy.Publisher('/py_controller/rear_left_wheel/encoder', JointState, queue_size=10)
	pubLeft.publish(left)
	rospy.spin()

   
  except rospy.ROSInterruptException:
    pass
