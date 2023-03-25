#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('purpose_session', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1) # 1hz
    #keep publishing until a Ctrl-C is pressed
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
