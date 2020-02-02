#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from opendlv_ros.msg import ActuationRequest

cmd_pub = rospy.Publisher("opendlv_cmd", ActuationRequest, queue_size=10)

def cmd_callback(cmd):
    opendlv_cmd = ActuationRequest()
    opendlv_cmd.delta_req = cmd.angular.z
    opendlv_cmd.ax_req = cmd.linear.x
    opendlv_cmd.header.stamp = rospy.Time.now()
    cmd_pub.publish(opendlv_cmd)

def cmd_translator():   
    rospy.init_node("cmd_translator", anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, cmd_callback)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()
    
if __name__ == '__main__':
    try:
        cmd_translator()
    except rospy.ROSInterruptException:
        pass