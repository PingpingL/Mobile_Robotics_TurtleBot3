#! /usr/bin/python
# Copyright (c) 2015, Rethink Robotics, Inc.

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import CompressedImage
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import numpy as np

import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'apriltag'])

import apriltag
print(dir(apriltag), vars(apriltag))

# Instantiate CvBridge
bridge = CvBridge()

def img_detector(gray_img, tag_size):
    # Calibration Parameters
    k = [999.461170663331, 996.9611451866272,
         642.2582577578172, 474.1471906434548]

    options = apriltag.DetectorOptions(families="tag36h11")
    detector = apriltag.Detector(options)
    results = detector.detect(gray_img)

    output = {}
    for r in results:
        M, init_error, final_error = detector.detection_pose(
            r, k, tag_size=tag_size)

        output[r.tag_id] = M

    return output


def image_callback(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.compressed_imgmsg_to_cv2(msg, "mono8")
        results = img_detector(cv2_img, tag_size=0.02)

        for tag_id, pose in results.items():
            print(tag_id, pose)
            # publish pose as twist vector
    except CvBridgeError as e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg
        cv2.imwrite('camera_image.jpeg', cv2_img)


def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/raspicam_node/image/compressed"

    print(f"Subscribing to {image_topic}")
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, CompressedImage, image_callback)

    print("Succesfully subscribed")

    # Spin until ctrl + c
    rospy.spin()


if __name__ == '__main__':
    main()
