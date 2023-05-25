import rospy
from geometry_msgs.msg import Twist

def rotate(event):
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=20)

#setting cmd to twist to create a rotate command that can be sent to the robot
    
    rot=Twist() # creates an instance where all twist messages are set to 0
    rot.angular.z = 0.6
    rotation_duration = (2*3.141592653589793)/rot.angular.z
    print(rotation_duration)

    # for i in range(int(rotation_duration)):
    #     print('hi')
    #     pub.publish(rot)
    
    start_time = rospy.get_time()
    while rospy.get_time() - start_time < rotation_duration:
    
        pub.publish(rot) # publish updated twist message to topic

# Revert back to original instance
    rot.angular.z = 0
    pub.publish(rot)# publish angular.z back to 0

rospy.init_node('Interruption')
rospy.Timer(rospy.Duration(10), rotate)
rospy.spin()

# #!/usr/bin/env python

# import rospy
# from geometry_msgs.msg import Twist
# from math import radians

# rospy.init_node('rotate_in_circle')

# pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

# twist = Twist()
# twist.angular.z = radians(45)  # 45 degrees per second, adjust as needed
# duration = 8.0  # duration in seconds
# rate = rospy.Rate(10)  # 10 Hz

# start_time = rospy.get_time()
# angle_rotated = 0

# while not rospy.is_shutdown() and angle_rotated < 360:
#     pub.publish(twist)
#     rate.sleep()

#     # Calculate the angle rotated
#     current_time = rospy.get_time()
#     angle_rotated = (current_time - start_time) * twist.angular.z * 180 / 3.14

# # Stop the robot
# twist = Twist()
# pub.publish(twist)