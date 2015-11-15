#!/usr/bin/python
import rospy
from sensor_msgs.msg import Range
import Adafruit_BBIO.ADC as ADC
import math
ADC.setup()

if __name__ == '__main__':
  try:
    rospy.init_node('irnode')
    global pub
    IR = Range()
    IR.header.frame_id="inertal_link"
    IR.radiation_type = 1
    IR.field_of_view = 3.14/5.0
    IR.min_range = 0.20
    IR.max_range = 1.5
    IR.range = None
    pub = rospy.Publisher('/range',Range, queue_size=10)
    while not rospy.is_shutdown():
        voltage = 0.0
        voltage = ADC.read("P9_39")
        value = voltage * 5.0
        distance = 59.23 * math.pow(value,-1.1597)
        distance = distance / 100.0
        print( distance)
	IR.range = distance
	rospy.loginfo(IR)
        pub.publish(IR)
    rospy.spin()
  except rospy.ROSInterruptException:
    pass
