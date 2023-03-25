#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def purpose_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    rospy.loginfo(rospy.get_caller_id() + "\nStudent listens' %s", "\nReceived message: " + message.data)
    
def subscriber():
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber("purpose_session", String, purpose_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()
