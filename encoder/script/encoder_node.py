#!/usr/bin/python
# Put the description of your file here
# Author: Theo Long <lziaho1@vt.edu>

# Import the Default ROS tools
import rospy
from sensor_msgs.msg import Range
import Adafruit_BBIO.ADC as ADC
import math
ADC.setup()

if __name__ == '__main__':
  try:
    rospy.init_node('irnode')
    global pub
    IRsensor.header.frame_id="inertal_link"
    IRsensor = Range()
    IRsensor.radiation_type = 1
    IRsensor.field_of_view = 3.14/5.0
    IRsensor.min_range = 0.20
    IRsensor.max_range = 1.5
    IRsensor.range = None
    pub = rospy.Publisher('/range',Range, queue_size=10)
    while not rospy.is_shutdown():
        voltage = 0.0
        voltage = ADC.read("P9_39")
        value = voltage * 5.0
        distance = 59.23 * math.pow(value,-1.1597)
        distance = distance / 100.0
        print distance
	IRsensor.range = distance
	rospy.loginfo(IRsensor)
        pub.publish(IRsensor)
    rospy.spin()
  except rospy.ROSInterruptException:
    pass
