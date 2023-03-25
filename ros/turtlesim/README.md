# ROS Activities

<p align="center">
<picture>
  <img alt="ROS Logo" src="../../ros-logo.webp" width="60%" hight="40%" >
</picture>
</p>

## ROS Example 2: TurtleSim Example

The following example is to work with `turtlesim node` which is attached in ROS packages.

### Compile packages

```sh
catkin_make
```

Run the ROS master node:

```sh
roscore
```

------------

### Run the `turtlesim_node`

```sh
rosrun turtlesim turtlesim_node
```

After running this command, you'll see a graphical representation for turtle.

<p align="center">
<picture>
  <img alt="Turtlesim Window" src="turtlesim_node.png" width="40%" hight="35%" >
</picture>
</p>

You'll notice that you can't control turtle movement.

------------

### Run the `turtle_teleop_key`

There is a built-in feature `turtle_teleop_key` that takes the keyboard input from the user and convert it to ROS msg that controls the turtle position:

```sh
rosrun turtlesim turtle_teleop_key
```

Now, you can control the turtle's position from your keyboard.

Take a look on the image below for drawing triangle using the turtle.

<p align="center">
<picture>
  <img alt="Turtlesim Window" src="turtlesim_with_teleop_node.png" width="70%" hight="60%" >
</picture>
</p>

#### Explore `turtlesim_node` info

Listing the nodes:

```sh
rosnode list
```

```sh
rosnode info /turtlesim
```

#### Explore `turtle` topics info

Listing the topics:

```sh
rostopic list
```

Listing the turtle command velocity topic:

```sh
rostopic info /turtle1/cmd_vel
```

Notice that the messages type of `cmd_vel` topic is `geometry_msgs/Twist`

#### Explore `Twist` message info

```sh
rosmsg show geometry_msgs/Twist
```

------------

### Exercises


#### Exercise 1

Explore info for `Pose` messages in `turtlesim` node.

#### Exercise 2

Try to figure out the purpose of this command:

```sh
rostopic echo /turtle1/cmd_vel
```

</br>
