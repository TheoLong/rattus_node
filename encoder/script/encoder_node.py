#!/usr/bin/python
# Put the description of your file here
# Author: Theo Long <lziaho1@vt.edu>

# Import the Default ROS tools
import rospy
from sensor_msgs.msg import Range
import Adafruit_BBIO.ADC as ADC
import math
ADC.setup()
encoderRight = QuadratureEstimator()
encoderLeft = QuadratureEstimator()
left1="P8_7"
left2="P8_8"
right1="P8_9"
right2="P8_10"
GPIO.setup(left1, GPIO.IN)
GPIO.setup(left2, GPIO.IN)
GPIO.setup(right1, GPIO.IN)
GPIO.setup(right2, GPIO.IN)
if __name__ == '__main__':
  try:
  	left=JointState()
  	right=JointState()
  	encoderr.update(GPIO.input(left1),GPIO.input(left2),rospy.get_rostime().to_sec)
	left.position.append(encoderr.position) 
	left.velocity.append(encoderr.velocity)
	encoderr.update(GPIO.input(right1),GPIO.input(right2),rospy.get_rostime().to_sec)
	left.position.append(encoderr.position) 
	left.velocity.append(encoderr.velocity)
	pubRight = rospy.Publisher('/py_controller/rear_right_wheel/encoder', JointState, queue_size=10)
	pubRight.publish(right)
	pubLeft = rospy.Publisher('/py_controller/rear_left_wheel/encoder', JointState, queue_size=10)
	pubr.publish(left)
	rospy.spin()

   
  except rospy.ROSInterruptException:
    pass
