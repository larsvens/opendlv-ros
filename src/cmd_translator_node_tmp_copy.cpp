#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "opendlv_ros/ActuationRequest.h"

opendlv_ros::ActuationRequest opendlv_cmd;  

void cmdCallback(const geometry_msgs::Twist::ConstPtr& cmd)
{
  std::cout << "in callback" << std::endl;
  opendlv_cmd.delta_req = cmd->angular.z;
  opendlv_cmd.ax_req = cmd->linear.x;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "cmd_translator_node");
  ros::NodeHandle n;
  ros::Publisher pub = n.advertise<opendlv_ros::ActuationRequest>("/lars/ActuationRequest", 1000);
  ros::Subscriber sub = n.subscribe("cmd_vel", 1000, cmdCallback);
  ros::Rate loop_rate(100);

  // initialize cmd to 0
  opendlv_cmd.delta_req = 0.0;
  opendlv_cmd.ax_req = 0.0;

  while (ros::ok())
  {
    pub.publish(opendlv_cmd);
    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}

	
