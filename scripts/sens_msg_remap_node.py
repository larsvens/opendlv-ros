#!/usr/bin/env python

import rospy
from opendlv_ros.msg import SensorMsgGPS
from opendlv_ros.msg import SensorMsgCAN 

class StateEstCart:
    def __init__(self):
        rospy.init_node('sens_msg_remap_node', anonymous=True)
        self.gps_sub = rospy.Subscriber("/OpenDLV/SensorMsgGPS", SensorMsgGPS, self.gps_callback)
        self.gps_msg = SensorMsgGPS()
        self.can_sub = rospy.Subscriber("/OpenDLV/SensorMsgCAN", SensorMsgCAN, self.can_callback)
        self.can_msg = SensorMsgCAN()
        self.gps_pub = rospy.Publisher('/OpenDLV/SensorMsgGPS_log', SensorMsgGPS, queue_size=1)
        self.can_pub = rospy.Publisher('/OpenDLV/SensorMsgCAN_log', SensorMsgCAN, queue_size=1)        
        
    def gps_callback(self,msg):
        self.gps_msg = msg
        self.gps_pub.publish(self.gps_msg)
        
    def can_callback(self,msg):
        self.can_msg = msg
        self.can_pub.publish(self.can_msg)

if __name__ == '__main__':
    
    sec = StateEstCart()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")   