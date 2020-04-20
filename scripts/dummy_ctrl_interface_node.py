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
        
        # uncomment to send nonzero values for first 5 seconds
        for i in range(500):
            self.odlv_cmd.acceleration = 20
            self.odlv_cmd.steering = 0.1           
            self.odlv_cmd.header.stamp = rospy.Time.now()
            self.odlv_cmd_pub.publish(self.odlv_cmd)
            self.rate.sleep()               
        
        # main loop
        while not rospy.is_shutdown(): 
            self.odlv_cmd.steering = self.cmd_vel.angular.z
            if(self.cmd_vel.linear.x >= 0):
                self.odlv_cmd.acceleration = 10.0*self.cmd_vel.linear.x # 0 to 30% throttle_req
            else:    
                self.odlv_cmd.acceleration = self.cmd_vel.linear.x      # 0 to -3.0m/s^2 brake_req
            self.odlv_cmd.header.stamp = rospy.Time.now()
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