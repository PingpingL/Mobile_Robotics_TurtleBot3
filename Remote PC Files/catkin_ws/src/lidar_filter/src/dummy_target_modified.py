import rospy
import numpy as np
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import Point, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib import SimpleActionClient
from tf.transformations import quaternion_from_euler
from visualization_msgs.msg import Marker

import tf2_ros
from geometry_msgs.msg import TransformStamped

def map_callback(msg):
    global map_data, map_info
    map_data = np.array(msg.data).reshape((msg.info.height, msg.info.width))
    map_info = msg.info

def sample_random_points(num_points):
    global map_data, map_info
    points = []

    while len(points) < num_points:
        x = np.random.randint(0, map_info.width)
        y = np.random.randint(0, map_info.height)

        if map_data[y][x] == 0:  # Free space
            px = x * map_info.resolution + map_info.origin.position.x
            py = y * map_info.resolution + map_info.origin.position.y
            points.append(Point(px, py, 0.0))

    return points

def create_move_base_goal(point):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position = point
    
    # Set orientation to face forward along the x-axis
    orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
    goal.target_pose.pose.orientation = orientation
    
    return goal

def send_goal_and_wait_for_result(client, goal):
    global tf_buffer
    range = 0.1
    current_positon = [0,0,0]
    distance = np.linalg.norm(current_position[:1]-goal[:1])
    for distance>range:
	    client.send_goal(goal)
	    transform = tf_buffer.lookup_transform('map','base_link',rospy.Time(0))
	    current_positon = transform.transform.translation
	    distance = np.linalg.norm(current_position[:1]-goal[:1])
    result = 3
    #client.send_goal(goal)
    #client.wait_for_result()
    return result#client.get_state()  # Return the state



def turn_360_degrees():
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    angular_speed = 0.5  # radians per second
    duration = 2 * np.pi / angular_speed  # time to complete a 360-degree turn

    twist = Twist()
    twist.angular.z = angular_speed
    start_time = rospy.Time.now()

    rate = rospy.Rate(10)  # Control loop rate: 10 Hz

    while (rospy.Time.now() - start_time).to_sec() < duration:
        vel_pub.publish(twist)
        rate.sleep()

    # Stop turning
    twist.angular.z = 0
    vel_pub.publish(twist)

def publish_marker(marker_pub, point, marker_id):
    marker = Marker()
    marker.header.frame_id = "map"
    marker.header.stamp = rospy.Time.now()
    marker.ns = "sample_points"
    marker.id = marker_id
    marker.type = Marker.SPHERE
    marker.action = Marker.ADD
    marker.pose.position.x = point.x
    marker.pose.position.y = point.y
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = 0.2
    marker.scale.y = 0.2
    marker.scale.z = 0.2
    marker.color.a = 1.0
    marker.color.r = 0.0
    marker.color.g = 1.0
    marker.color.b = 0.0

    marker_pub.publish(marker)

if __name__ == '__main__':
    rospy.init_node('random_sampler')
    map_subscriber = rospy.Subscriber('/map', OccupancyGrid, map_callback)
    
    # current tf
    global tf_buffer,tf_listener
    tf_buffer = tf_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    
    # Wait for the map to be received
    rospy.wait_for_message('/map', OccupancyGrid)
    
    num_points = 10  # Number of random points to sample
    random_points = sample_random_points(num_points)

    move_base_client = SimpleActionClient('move_base', MoveBaseAction)
    move_base_client.wait_for_server()

    marker_pub = rospy.Publisher('/visualization_marker', Marker, queue_size=10)  
    rospy.sleep(1)
    marker_id = 0  

    for point in random_points:
        print(f"Moving to point: x={point.x}, y={point.y}")

        # Add the following two lines
        publish_marker(marker_pub, point, marker_id)
        marker_id += 1

        # Send the robot to the random point
        goal = create_move_base_goal(point)
        result = send_goal_and_wait_for_result(move_base_client, goal)

        # Check if the robot reached the goal successfully
        print(f"Result: {result}")
        if result == 3:  # GoalStatus.SUCCEEDED = 3
            print("Reached point successfully. Performing 360-degree turn.")
            turn_360_degrees()
        else:
            print("Failed to reach the point. Moving to the next point.")
