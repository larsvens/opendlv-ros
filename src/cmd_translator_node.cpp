#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "opendlv_ros/ActuationRequest.h"

class CmdTranslator{
public:
    CmdTranslator() 
    {
        pub_ = nh_.advertise<opendlv_ros::ActuationRequest>("/lars/ActuationRequest", 1);
        sub_ = nh_.subscribe("cmd_vel", 1, &CmdTranslator::cmdCallback, this);
    };

    void cmdCallback(const geometry_msgs::Twist::ConstPtr& cmd){
        opendlv_cmd_.steering = cmd->angular.z;
        opendlv_cmd_.acceleration = cmd->linear.x;
        pub_.publish(opendlv_cmd_);
    };
   
private:
    ros::NodeHandle nh_;
    ros::Subscriber sub_;
    ros::Publisher pub_;
    opendlv_ros::ActuationRequest opendlv_cmd_;

}; // end of class

int main(int argc, char **argv)
{
    ros::init(argc, argv, "cmd_translator_node");
    CmdTranslator cmdtrl;
    ros::spin();
    return 0;
}	
