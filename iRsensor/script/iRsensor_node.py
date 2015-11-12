#!/usr/bin/python
# Put the description of your file here
# Author: theo <lzihao1@vt.edu>

# Import the Default ROS tools
import rospy
from sensor_msgs.msg import Range
import Adafruit_BBIO.ADC as ADC
import math
ADC.setup()

if __name__ == '__main__':
  try:
    #Initialize node
    rospy.init_node('iRsensor_node')
    # Declare we are using the pub defined above, not a new local variable
    global pub
    
    pub = rospy.Publisher('/range',Range, queue_size=10)
    while not rospy.is_shutdown():
        value = 0.0
        value = ADC.read("P9_39")
        voltage = value * 5.0
        distance = 59.3 * math.pow(voltage,-1.1597)
        distance = distance / 100
        print distance
	IRsensor = Range()
	IRsensor.INFRARED = 1
	IRsensor.min_range = 0.20
	IRsensor.max_range = 1.5
	IRsensor.range = distance
        pub.publish(IRsensor)
    #We need to wait for new messages
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass
