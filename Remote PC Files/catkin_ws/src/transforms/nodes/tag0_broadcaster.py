import rospy, geometry_msgs.msg
import tf as tf2_ros

if __name__ == '__main__':
  rospy.init_node('tag0_listener')
  #tfBuffer = tf2_ros.Buffer()
  listener = tf2_ros.TransformListener()#tfBuffer)
  rate = rospy.Rate(10.0)
  tag_ids = ['tag_0', 'tag_1', 'tag_2', 'tag_3', 'tag_4', 'tag_5', 'tag_6']

  while not rospy.is_shutdown():
    for tag_id in tag_ids:

      try:
        (trans,rot) = listener.lookupTransform('map', tag_id, \
          rospy.Time(0))
        print(trans, rot)
        tf2Broadcast = tf2_ros.TransformBroadcaster()
        tf2Stamp = geometry_msgs.msg.TransformStamped()
        tf2Stamp.header.stamp = rospy.Time.now()
        tf2Stamp.header.frame_id = 'map'
        tf2Stamp.child_frame_id = 'tag_0'
        tf2Stamp.transform.translation = trans
        tf2Stamp.transform.rotation = rot
        tf2Broadcast.sendTransform(trans, rot, rospy.Time(0), tag_id, 'map')

# This will give you the coordinate of the child in the parent frame
      except (tf2_ros.LookupException, tf2_ros.ConnectivityException,
      tf2_ros.ExtrapolationException) as e:
        print(e)
  rate.sleep()
