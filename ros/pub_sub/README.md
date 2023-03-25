# ROS Activities

<p align="center">
<picture>
  <img alt="ROS Logo" src="../../ros-logo.webp" width="60%" hight="40%" >
</picture>
</p>


## ROS Example 1: Publisher/Subscriber

The following example is tested on ROS Kinetic on Ubuntu 16.04 (Xenial).

### Clone the repo:

In your terminal (ROS on Ubuntu OS), clone the repo from the link using this command:

```sh
git clone https://github.com/MeqdadDev/hello-ros1
```

------------

### Preparing workspace

Copy the files in `ros_demo/src/pub_sub_example` into your `src` package directory.

As a result, `src` directory in your package should have: `publisher.py`, `subscriber.py`

Now, open your workspace in the code editor (VS Code). Let's assume you're working on `meqdad_ws` workspace, and your package name is `ros_demo`.

Open the terminal and change the directory to `meqdad_ws` as in the command below:

```sh
cd meqdad_ws/
```

------------

### Compile packages

After adding `publisher.py`, `subscriber.py` into your `src` directory, run the compilation command for packages:

```sh
catkin_make
```

And finally, don't forget to run the ROS master node:

```sh
roscore
```

------------

### Publisher

In this example, we assume the following settings:
- Publisher node name: `publisher`
- Topic name: `session`
- Message type: `string`

```python
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('session', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    ctr = 0
    while not rospy.is_shutdown():
        hello_str = "Meqdad speaks %s" % ctr
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        ctr+=1

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
```

------------

### Subscriber

In this example, we assume the following settings:
- Subscriber node name: `subscriber`
- Topic name: `session`
- Message type: `string`

```python
import rospy
from std_msgs.msg import String

def purpose_callback(message):
    rospy.loginfo(rospy.get_caller_id() + "\nStudent listens' %s", "\nReceived message: " + message.data)
    
def subscriber():
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber("session", String, purpose_callback)

    rospy.spin()

if __name__ == '__main__':
    subscriber()
```

------------

### Explore Nodes and Topics

```sh
rosnode list
```

```sh
rostopic list
```

------------

### RQT Graphical Represntation

You can draw a graphical representation for the running topics and connected nodes using `rqt` GUI plugin.

```sh
rosrun rqt_graph rqt_graph
```


</br>
