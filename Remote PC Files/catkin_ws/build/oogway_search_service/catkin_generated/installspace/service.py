import rospy
import numpy as np
from geometry_msgs.msg import Twist
from oogway_search_service.srv import service, serviceResponse
from actionlib_msgs.msg import GoalStatusArray, GoalID
from std_msgs.msg import Empty

goal_status = GoalStatusArray()

def status_callback(status_msg):
	global goal_status
	goal_status = status_msg

def handle_oogway_service(req):
	global goal_status

	interrupt_pub.publish(GoalID())

	rospy.sleep(0.1)

	rot = Twist()
	rot.angular.z = 0.8
	rot_duration = (2*np.pi)/0.8

	start1 = rospy.Time.now()
	seconds1 = start1.to_sec()
	print('1')
	print(type(seconds1))
	#if rospy.time.now() - start_time1 > 9:
	#	start_time2 = rospy.time.now()
	while rospy.Time.now() - seconds1 < rot_duration:
		pub.publish(rot)
		print('2')
	resume_pub.publish(Empty())

	return serviceResponse(success=True)

if __name__ == '__main__':
	print('3')
	rospy.init_node('oogway_search_service')
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
	interrupt_pub = rospy.Publisher('/move_base/cancel',GoalID, queue_size=1)
	resume_pub = rospy.Publisher('move_base/resume', Empty, queue_size=1)
	rospy.Service('service', service, handle_oogway_service)
	rospy.Subscriber('move_base/status', GoalStatusArray, status_callback)
	rospy.spin()
