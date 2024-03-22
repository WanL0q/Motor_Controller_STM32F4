#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt8

def main():
    rospy.init_node('stm32_publisher')
    pub = rospy.Publisher('velocity_set', UInt8, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        velocity = input("Enter velocity (0-255): ")
        if 0 <= velocity <= 255:
            pub.publish(velocity)
            rospy.loginfo("Published velocity: %d", velocity)
        else:
            rospy.logerr("Velocity out of range. Please enter a value between 0 and 255.")
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

