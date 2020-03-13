#include "ros/ros.h"
#include "opendlv_ros/ActuationRequest.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "lars");

  ros::NodeHandle n;

  ros::Publisher pub = n.advertise<opendlv_ros::ActuationRequest>("/lars/ActuationRequest", 1000);

  // 1Hz
  ros::Rate loop_rate(1);

  int count = 0;
  while (ros::ok())
  {
    opendlv_ros::ActuationRequest msg;
    msg.delta_req = count;
    msg.ax_req = -count;

    pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }


  return 0;
}
