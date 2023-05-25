#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_srvs.srv import Trigger, TriggerResponse


def handle_rotate_360(req):
    #Function call
    rotate_360()
    #Return a TriggerResponse with a printed message ensuring success of rotation (not required)
    return TriggerResponse(success=True, message="Robot rotated 360 degrees.")

def rotate_360():
    #Initialize the Twist message 
    twist_msg = Twist()
    #Set angular velocity of turtlebot to make a 360 degrees rotation
    twist_msg.angular.z = 0.5
    #Publish the Twist message to the turtlebot's cmd_vel topic
    cmd_vel_pub.publish(twist_msg)
    #Rotate every 7 seconds 
    rospy.sleep(7)
    #Stop rotation
    twist_msg.angular.z = 0
    #publish Twist message
    cmd_vel_pub.publish(twist_msg)

if __name__ == '__main__':
    #Initialize ROS node
    rospy.init_node('rotate_node')
    # Create publisher for the cmd_vel topic
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    # Create a service for the rotate_360 function
    rotate_service = rospy.Service('/rotate_360', Trigger, handle_rotate_360)
    #Spin the ROS node to wait for service
    rospy.spin()


