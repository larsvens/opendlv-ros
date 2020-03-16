#!/usr/bin/env python

'''
Description: Estimate tamp state (s, d, deltapsi, psidot, vx, vy) from opendlv sensor data
'''

#import numpy as np
import rospy
#from common.msg import State
from opendlv_ros.msg import SensorMsgGPS
from opendlv_ros.msg import SensorMsgCAN


class StateEst:
    # constructor
    def __init__(self):
        
        rospy.init_node('state_est_opendlv', anonymous=True)
        self.dt = 0.1
        self.rate = rospy.Rate(1/self.dt)

        self.gpsmsg_sub = rospy.Subscriber("OpenDLV/SensorMsgGPS", SensorMsgGPS, self.gpsmsg_callback)
        self.gpsmsg = SensorMsgGPS
        self.gpsmsg_received = False
        self.canmsg_sub = rospy.Subscriber("OpenDLV/SensorMsgCAN", SensorMsgCAN, self.canmsg_callback)
        self.canmsg = SensorMsgCAN
        self.canmsg_received = False

        # wait for messages before entering main loop
        while(not self.gpsmsg_received):
            rospy.loginfo_throttle(1, "waiting for gps msg")
            self.rate.sleep()
        while(not self.canmsg_received):
            rospy.loginfo_throttle(1, "waiting for can msg")
            self.rate.sleep()
            
        # main loop
        while not rospy.is_shutdown(): 
            self.rate.sleep()


    def gpsmsg_callback(self, msg):
        self.gpsmsg = msg 
        print "lat = " , self.gpsmsg.latitude
        print "lon = " , self.gpsmsg.longitude
        self.gpsmsg_received = True

    def canmsg_callback(self, msg):
        self.canmsg = msg 
        #print "self.canmsg = " , self.canmsg
        self.canmsg_received = True

if __name__ == '__main__':
    sem = StateEst()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")   