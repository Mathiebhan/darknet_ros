# Train your own weights
For labellin you can use BBOX or anything that is friendly with YOLO

I recommend looking into: https://github.com/AlexeyAB/darknet

# YOLO ROS: Real-Time Object Detection for ROS

The YOLO packages have been tested under ROS Melodic and Jetpack 4.5 (Ubuntu 18.04/also headless) with a Jetson Nano Developer Kit.


### Installation

In order to install darknet_ros, clone the latest version using SSH (see [how to set up an SSH key](https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html)) from this repository into your catkin workspace and compile the package using ROS.

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

### Yolov3-tiny

![alt text](https://github.com/Mathiebhan/darknet_ros/blob/master/2.png)


### Yolov4-tiny

![alt text](https://github.com/Mathiebhan/darknet_ros/blob/master/1.png)

    

