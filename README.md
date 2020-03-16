# opendlv_ros
Tested on Ubuntu 16.04 and ROS Kinetic.   
ROS Kinetic install: http://wiki.ros.org/kinetic/Installation/Ubuntu   
Create a catkin workspace: http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment   
Pull the opendlv-ros package to your workspace:   
`cd ~/catkin_ws/src`   
`git clone git@github.com:larsvens/opendlv-ros.git`   

Build and source:   
`cd ~/catkin_ws`   
`catkin_build`   
`source devel/setup.bash`   

Launch command publisher:   
`roslaunch opendlv_ros ros_cmd_to_opendlv_test.launch`   
