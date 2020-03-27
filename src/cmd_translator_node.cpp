#include "ros/ros.h"
#include "opendlv_ros/ActuationRequest.h"

class CmdTranslator{
public:
    CmdTranslator() 
    {
        pub_ = nh_.advertise<opendlv_ros::ActuationRequest>("/lars/ActuationRequest", 1);
        sub_ = nh_.subscribe("/OpenDLV/ActuationRequest", 1, &CmdTranslator::cmdCallback, this);
    };

    void cmdCallback(const opendlv_ros::ActuationRequest::ConstPtr& opendlv_cmd){
        opendlv_cmd_.steering = opendlv_cmd->steering;
        opendlv_cmd_.acceleration = opendlv_cmd->acceleration;
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
