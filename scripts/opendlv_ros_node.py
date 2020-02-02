#!/usr/bin/env python
import rospy
from opendlv_ros.msg import ActuationRequest
from opendlv_ros.msg import SensorMsgCAN
from opendlv_ros.msg import SensorMsgGPS

class OpenDLV_ROS:

    def __init__(self):
        rospy.init_node('opendlv_ros_interface', anonymous=True)
        self.rate = rospy.Rate(100)
        
        self.can_pub = rospy.Publisher('/opendlv_can_data', SensorMsgCAN, queue_size=10)
        self.sensor_msg_can = SensorMsgCAN()
        
        self.gps_pub = rospy.Publisher('/opendlv_gps_data', SensorMsgGPS, queue_size=10)
        self.sensor_msg_gps = SensorMsgGPS()

        self.cmd_sub = rospy.Subscriber("opendlv_cmd", ActuationRequest, self.cmd_callback)
        self.actuation_request = ActuationRequest()
        
        while not rospy.is_shutdown():

            # publish can data
            self.sensor_msg_can.header.stamp = rospy.Time.now()
            # todo here: update values in self.sensor_msg_can 
            self.can_pub.publish(self.sensor_msg_can)
            
            # publish gps data
            self.sensor_msg_gps.header.stamp = rospy.Time.now()
            # todo here: update values in self.sensor_msg_gps 
            self.gps_pub.publish(self.sensor_msg_gps)

            # pass cmd to opendlv
            rospy.loginfo_throttle(0.1,"delta_request: %f" %self.actuation_request.delta_req)
            rospy.loginfo_throttle(0.1,"ax_request:    %f" %self.actuation_request.ax_req)
            # todo here: pass cmd to opendlv
            
            self.rate.sleep()

    def cmd_callback(self,msg):
        self.actuation_request = msg
        
if __name__ == '__main__':
    opendlvros = OpenDLV_ROS()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")   
    