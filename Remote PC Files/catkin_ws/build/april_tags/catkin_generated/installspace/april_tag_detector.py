#! /usr/bin/python

import numpy as np
import cv2  # use python3.8.5
import apriltag


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

