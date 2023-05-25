import rospy
import tf2_ros
import geometry_msgs.msg

def





if __name__ == '__main__':
	rospy.init_node('tag_publisher')
	pub = rospy.Publisher('/tag_frams', geometry_msgs.msg.Twist, queue_size = 1)
	tfBuffer = tf2_ros.Buffer()
	listener = tf2_ros.TransformListener(tfBuffer)
	rate = rospy.Rate(10.0)
	while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform(turtle_name, 'turtle1', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
        	rate.sleep()
        	continue
        msg = geometry_msgs.msg.Twist()
	pub.pubish(msg)
