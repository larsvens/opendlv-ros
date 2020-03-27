#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from opendlv_ros.msg import ActuationRequest

# Descrition: Dummy ctrl interface 
# subscribing to cmd_vel
# publishing ActuationRequest @ 100Hz

class CtrlInterface:
    def __init__(self):
        
        # init
        rospy.init_node('dummy_ctrl_interface', anonymous=True)
        self.cmdvel_sub = rospy.Subscriber("/cmd_vel", Twist, self.cmdvel_callback)
        self.odlv_cmd_pub = rospy.Publisher('/OpenDLV/ActuationRequest', ActuationRequest, queue_size=1)
        self.rate = rospy.Rate(100)
        self.cmd_vel = Twist()
        self.odlv_cmd = ActuationRequest()    

        # loop
        while not rospy.is_shutdown(): 
            self.odlv_cmd.steering = self.cmd_vel.angular.z
            self.odlv_cmd.acceleration = self.cmd_vel.linear.x
            self.odlv_cmd_pub.publish(self.odlv_cmd)
            self.rate.sleep()

    def cmdvel_callback(self, msg):
        self.cmd_vel = msg 

if __name__ == '__main__':
    ci = CtrlInterface()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")