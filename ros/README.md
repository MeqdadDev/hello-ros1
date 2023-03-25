# ROS Activities

<p align="center">
<picture>
  <img alt="ROS Logo" src="../ros-logo.webp" width="60%" hight="40%" >
</picture>
</p>


## Robot Operating System - ROS

### Installing Required ROS Packages:

Just copy and paste the following commands in the terminal in your Ubuntu OS.

------------

#### Setup your sources.list
```sh
sudo apt install curl
```

------------

#### Set up your keys
```sh
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

------------

#### Installation

Make sure your OS package index is up-to-date:

```sh
sudo apt-get update
```

------------

#### Desktop-Full Install: (Recommended)

```sh
sudo apt-get install ros-kinetic-desktop-full
```

------------

#### Environment setup

```sh
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc

source ~/.bashrc
```

------------

#### Dependencies for building packages
```sh
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

------------

#### Initialize rosdep
```sh
sudo rosdep init

rosdep update
```

------------

#### Test Environment Setup

At home directory, take a look on ```bashrc``` to check out the ```setup.bash```

```sh
gedit .bashrc
```

You should find  ```source /opt/ros/kinetic/setup.bash``` at the end of file.

------------

#### Create Workspace

```sh
mkdir -p ~/meqdad_ws/src

cd meqdad_ws/
```

compile the default files

```sh
catkin_make
```

Run ROS master

```sh
roscore
```

Explore the default topics

```sh
rostopic list
```

It is not recommended to make all your ROS projects in one workspace.

One of the best practices is to customize the workspace for your ```setup.bash``` file

```sh
gedit .bashrc

source /home/meqdad/meqdad_ws/devel/setup.bash
```

#### Create package

```sh
cd meqdad_ws/src

catkin_create_pkg ros_demo std_msgs rospy roscpp
```

Default packages (```std_msgs rospy roscpp```)

Our created package (```ros_demo```)

Compile created package

```sh
cd meqdad_ws/

catkin_make
```

### ROS Examples:

<ul>
  <li><a href="pub_sub\README.md">Publisher/Subscriber Example</a></li>
  <li><a href="turtlesim\README.md">TurtleSim Example</a></li>
  <li><a href="turtlebot_rviz\README.md">TurtleBot RViz Example</a></li>
</ul>

</br>
