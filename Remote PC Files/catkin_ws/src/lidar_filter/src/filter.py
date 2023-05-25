#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
def _init_(self):
    print('1')
   
        
        
def scan_callback(scan_msg):
    # print(scan_msg)
    # print('2')
    angle_min = 1#rospy.get_param('~angle_min', 0) # default to -90 degrees
    angle_max = 5#rospy.get_param('~angle_max', 0)  # default to 90 degrees
    
    # Convert the angle range to indices in the ranges array
    # print(scan_msg)
    filtered_ranges = list(scan_msg.ranges)
    # angle_increment = scan_msg.angle_increment
    # angle_start = scan_msg.angle_min
    # angle_end = scan_msg.angle_max
    # index_start = int((angle_start - angle_min) / angle_increment)
    # index_end = int((angle_end - angle_max) / angle_increment)

    # Filter the scan data to only include scans within the specified angle range
    # filtered_ranges = ranges[index_start:index_end]
    filtered_ranges[30:330] = [0]*300
    print('success')
    scan_msg.ranges = filtered_ranges
    # scan_msg.ranges = filtered_ranges
    # scan_msg.angle_min=angle_min
    # scan_msg.angle_max=angle_max
    pub.publish(scan_msg)
    # pub2.publish('hi')
    # print(filtered_ranges)

if __name__ == '__main__':
    # pub2 = rospy.Publisher('/scan', String, queue_size=1 )
    pub = rospy.Publisher('/full_scan', LaserScan, queue_size = 10)
    rospy.init_node('PREM')
    scan_sub = rospy.Subscriber('/scan', LaserScan, scan_callback)

    # print('3')
    
    rospy.spin()
