#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray

def stm32_interface():
    rospy.init_node('stm32_interface', anonymous=True)

    # Publisher
    cmd_vel = rospy.Publisher("cmd_vel", Float32MultiArray, queue_size=10)

    rate = rospy.Rate(1) 

    while not rospy.is_shutdown():
        
        v_x = float(input("Enter velocity along x-axis: "))
        v_y = float(input("Enter velocity along y-axis: "))
        w_z = float(input("Enter angular velocity along z-axis: "))

        # Tạo một đối tượng Float32MultiArray
        vel_msg = Float32MultiArray()
        
        # Gán dữ liệu vào danh sách data
        vel_msg.data = [v_x, v_y, w_z]
        
        # Xuất bản thông điệp
        cmd_vel.publish(vel_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        stm32_interface()
    except rospy.ROSInterruptException:
        pass

