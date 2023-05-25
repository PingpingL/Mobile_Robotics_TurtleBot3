#!/usr/bin/env python3
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg

from apriltag_ros.msg import AprilTagDetectionArray


def handle_tag_pose(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "camera_link"
    

    for detection in msg.detections:
        t.child_frame_id = "tag_" + str(detection.id[0])
        pose = detection.pose.pose.pose

        t.transform.translation.x = pose.position.z
        t.transform.translation.y = -pose.position.x
        t.transform.translation.z = -pose.position.y

        t.transform.rotation.x = pose.orientation.x
        t.transform.rotation.y = pose.orientation.y
        t.transform.rotation.z = pose.orientation.z
        t.transform.rotation.w = pose.orientation.w

        print(t)
        br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tag_tf2_broadcaster')
    rospy.Subscriber('/tag_detections', AprilTagDetectionArray, handle_tag_pose, queue_size=1)
    rospy.spin()
