#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class OpenDLV_ROS:

    def __init__(self):
        rospy.init_node('opendlv_ros_interface', anonymous=True)
        self.rate = rospy.Rate(100)
        self.cmd_sub = rospy.Subscriber("cmd_vel", Twist, self.cmd_callback)
        self.ax_request = 0
        self.delta_request = 0
        
        while not rospy.is_shutdown():
            rospy.loginfo("delta_request: %f" %self.delta_request)
            rospy.loginfo("ax_request:    %f" %self.ax_request)
            self.rate.sleep()

    def cmd_callback(self,msg):
        self.delta_request = msg.angular.z
        self.ax_request = msg.linear.x
        
if __name__ == '__main__':
    opendlvros = OpenDLV_ROS()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")   
    