#!/usr/bin/env python3

import cv2
import imutils
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image

class PeopleDetector:

    def __init__(self):
        rospy.init_node('people_detector')

        self.bridge = CvBridge()

        # Load the pre-trained person detector
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        self.image_pub = rospy.Publisher('processed_image', Image, queue_size=10)
        self.image_sub = rospy.Subscriber('usb_cam/image_raw', Image, self.image_callback)

    def image_callback(self, msg):
        # Convert ROS Image message to OpenCV image
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Perform people detection and draw bounding boxes
        processed_image = self.detect_people(cv_image)

        # Convert the processed OpenCV image to ROS Image message
        ros_image = self.bridge.cv2_to_imgmsg(processed_image, encoding='bgr8')

        # Publish the processed ROS Image message to a new topic
        self.image_pub.publish(ros_image)

    def detect_people(self, image):
        # Resize the image to a fixed width (while maintaining the aspect ratio)
        image_resized = imutils.resize(image, width=min(400, image.shape[1]))

        # Detect people in the image
        (rects, weights) = self.hog.detectMultiScale(image_resized, winStride=(4, 4), padding=(8, 8), scale=1.05)

        # Draw bounding boxes around the detected people
        for (x, y, w, h) in rects:
            # Scale the coordinates back to the original image size
            x = int(x * (image.shape[1] / float(image_resized.shape[1])))
            y = int(y * (image.shape[0] / float(image_resized.shape[0])))
            w = int(w * (image.shape[1] / float(image_resized.shape[1])))
            h = int(h * (image.shape[0] / float(image_resized.shape[0])))
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return image


if __name__ == '__main__':
    try:
        pd = PeopleDetector()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
