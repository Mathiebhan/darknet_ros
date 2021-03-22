# Train your own weights (Can be done on Windows, Linux and Colab)
For labelling you can use BBOX or anything that is friendly with YOLO

How to get started: https://drive.google.com/file/d/1L6AJDgrG3DzuDQhHzu-XnsHfL6SJSOyP/view?usp=sharing

I recommend looking into: https://github.com/AlexeyAB/darknet

BBOX for labelling: https://drive.google.com/file/d/1zy2duo2lZXkVcst5DWbmQPmHPeLnQ-Gj/view?usp=sharing

-------------------------------------------------------------------------------------------------------------------------------------------------------------
### Datasets used are from: 

- https://www.immersivelimit.com/datasets/cigarette-butts
- https://www.kaggle.com/estebanpacanchique/cigarette-butt

--------------------------------------------------------------------------------------------------------------------------------------------

# YOLO ROS: Real-Time Object Detection for ROS

The YOLO packages have been tested under ROS Melodic and Jetpack 4.5 (Ubuntu 18.04/also headless) with a Jetson Nano Developer Kit.


### Installation

In order to install darknet_ros, clone the latest version using SSH (see [how to set up an SSH key](https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html)) from this repository into your catkin workspace and compile the package using ROS.


!!!!ALERT THIS ONLY WORKS FOR opencv3.4!!!!!!
Use this repo for opencv4 https://github.com/kunaltyagi/darknet_ros/tree/opencv4 but only yolov2-v3 works

    cd catkin_workspace/src
    git clone --recursive git@github.com:mathiebhan/darknet_ros.git
    cd ../

To maximize performance, make sure to build in *Release* mode. You can specify the build type by setting

    catkin_make -DCMAKE_BUILD_TYPE=Release

or using the [Catkin Command Line Tools](http://catkin-tools.readthedocs.io/en/latest/index.html#)

    catkin build darknet_ros -DCMAKE_BUILD_TYPE=Release

### Weights for cigarette butts
The weights can be downloaded from my drive.

https://drive.google.com/drive/folders/1FedP8PPMcz5fOFMcLrToPjFqonRJZlUE


### Use your own detection objects

In order to use your own detection objects you need to provide your weights and your cfg file inside the directories:

    catkin_workspace/src/darknet_ros/darknet_ros/yolo_network_config/weights/
    catkin_workspace/src/darknet_ros/darknet_ros/yolo_network_config/cfg/

In addition, you need to create your config file for ROS where you define the names of the detection objects. You need to include it inside:

    catkin_workspace/src/darknet_ros/darknet_ros/config/

Then in the launch file you have to point to your new config file in the line:

    <rosparam command="load" ns="darknet_ros" file="$(find darknet_ros)/config/your_config_file.yaml"/>
    
Of course usb_cam is needed from ROS https://github.com/ros-drivers/usb_cam (sudo apt install ros-melodic-usb-cam) and CSI cam from https://github.com/sfalexrog/jetson_camera 

### Yolov3-tiny

![alt text](https://github.com/Mathiebhan/darknet_ros/blob/master/2.png)


### Yolov4-tiny

![alt text](https://github.com/Mathiebhan/darknet_ros/blob/master/1.png)

    

